FROM alpine/git AS pytorch-source

# Carefully select commit hash, as they are not guaranteed to uniformly build successfully.

RUN git clone https://github.com/pytorch/pytorch.git pytorch && \
    cd pytorch && \
    git checkout 7919f0b && \
    git submodule update --init --recursive && \
    cd ..

FROM nvidia/cuda:12.5.1-cudnn-devel-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive

# For this Dockerefile we will use pyenv. Installing Python via pyenv creates an isolated environment, separate from
# Ubuntu's system Python. This approach prevents accidental modifications to system-critical components that rely on
# the default Python, ensuring overall system stability and avoiding potential breakage of Ubuntu's built-in tools and
# packages. It also provides us with flexibility to choose any desired Python version.

# Install essential build packages for Python (built by pyenv) and PyTorch, as they are built from source.
# Additional utility packages (curl, git, wget) are included for common development tasks.
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        ca-certificates \
        cmake \
        curl \
        git \
        libbz2-dev \
        libffi-dev \
        liblzma-dev \
        libncurses5-dev \
        libncursesw5-dev \
        libreadline-dev \
        libsqlite3-dev \
        libssl-dev \
        libxml2-dev \
        libxmlsec1-dev \
        llvm \
        ninja-build \
        openssh-client \
        tk-dev \
        wget \
        xz-utils \
        zlib1g-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# pyenv configuration
ENV PYENV_GIT_TAG="v2.4.7"
ENV PYENV_ROOT=/root/.pyenv
ENV PATH="$PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH"

ENV PYTHON_VERSION=3.12.3

RUN curl https://pyenv.run | bash && pyenv install $PYTHON_VERSION

WORKDIR /app

RUN pyenv local $PYTHON_VERSION

ENV PIP_INSTALL_VERSION=24.1.2
ENV POETRY_VERSION=1.8.3

RUN pip install --upgrade pip==$PIP_INSTALL_VERSION && \
    pip install --no-cache-dir poetry==$POETRY_VERSION && \
    pip cache purge

# Set up environment for PyTorch build
ENV USE_CUDA=1
ENV USE_CUDNN=1
ENV CMAKE_PREFIX_PATH="$(dirname $(which python))/../"

COPY --from=pytorch-source git/pytorch pytorch
COPY pyproject.toml poetry.toml poetry.lock ./
RUN poetry install --no-root && poetry add -e -vvv ./pytorch && rm -rf pytorch

EXPOSE 8888
CMD ["poetry", "run", "jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
