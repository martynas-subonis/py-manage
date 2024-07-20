FROM alpine/git AS pytorch-source

RUN git clone --depth 1 --recursive https://github.com/pytorch/pytorch.git pytorch && \
    cd pytorch && \
    git submodule sync && \
    git submodule update --init --recursive && \
    cd ..

FROM nvidia/cuda:12.5.1-cudnn-devel-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive

# Install build essentials for Python (needed for pyenv) and PyTorch, plus common dev tools.
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
        libmkl-full-dev \
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

# Here pyenv is used to create an isolated Python environment, separate from the system Python. This approach
# ensures system stability, prevents conflicts with Ubuntu's built-in tools, and provides flexibility in choosing
# Python versions.

# pyenv/poetry setup
ENV PYENV_GIT_TAG="v2.4.7" \
    PATH="/root/.pyenv/shims:/root/.pyenv/bin:$PATH" \
    PYTHON_VERSION=3.12.3 \
    PIP_INSTALL_VERSION=24.1.2 \
    POETRY_VERSION=1.8.3

WORKDIR /app

RUN curl https://pyenv.run | bash && \
    pyenv install $PYTHON_VERSION && \
    pyenv local $PYTHON_VERSION && \
    pip install --upgrade pip==$PIP_INSTALL_VERSION && \
    pip install --no-cache-dir poetry==$POETRY_VERSION && \
    pip cache purge

# PyTorch build configuration:
# https://docs.nvidia.com/cuda/cuda-compiler-driver-nvcc/index.html#gpu-feature-list
# CUDA_ARCH_LIST specifies target GPU architectures (e.g., Turing: sm_75)
# Adjust MAX_JOBS based on available system resources
# Remove DEBUG flag if not needed.

ENV USE_CUDA=1 \
    USE_CUDNN=1 \
    CMAKE_PREFIX_PATH="/root/.pyenv/versions/$PYTHON_VERSION" \
    TORCH_CUDA_ARCH_LIST="7.5" \
    MAX_JOBS=12 \
    DEBUG=1

COPY pyproject.toml poetry.toml poetry.lock ./
COPY --from=pytorch-source git/pytorch pytorch
# Install dependencies and PyTorch from source. PyTorch is installed via pip to significantly
# improve build time. We omit creating a .lock file for this installation since the resulting
# environment state won't be further distributed.
RUN poetry install --no-root && \
    . .venv/bin/activate && \
    pip install -v ./pytorch && \
    deactivate && \
    rm -rf pytorch

EXPOSE 8888
CMD ["poetry", "run", "jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]