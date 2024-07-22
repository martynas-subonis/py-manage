# py-manage

A personal, opinionated guide to managing Python projects. Literature that extends the argumentation and explains it on 
a more detailed level:
- ["Python Project Management Primer"](https://martynassubonis.substack.com/p/python-project-management-primer).
- ["Optimizing Docker Images for Python Production Services"](https://martynassubonis.substack.com/p/optimizing-docker-images-for-python).

## Table of Contents

1. [Tooling](#tooling)
2. [Dockerfile Optimizations](#dockerfile-optimizations)
3. [CUDA Development Workbenches](#cuda-development-workbenches)
4. [Standard Project Structure](#standard-project-structure)
5. [Mono-Repository Structure](#mono-repository-structure)
6. [Workflows](#workflows)
    1. [Starting a New Project](#starting-a-new-project)
    2. [Installing an Existing Project](#installing-an-existing-project)
    3. [Developing Locally](#developing-locally)
    4. [Building Docker Images](#building-docker-images)
    5. [Running Docker Containers Locally](#running-docker-containers-locally)
    6. [CI/CD](#cicd)

## Tooling

- Use [pyenv](https://github.com/pyenv/pyenv) to manage `Python` versions.
- Use [pipx](https://github.com/pypa/pipx) to install and run global `Python` applications in isolated
  environments (`poetry` for example).
- Use [poetry](https://github.com/python-poetry/poetry) to manage `Python` dependencies and packaging.
- [minor] use [ruff](https://github.com/astral-sh/ruff) as a linter/formatter.

## Dockerfile Optimizations

This guide recommends the following techniques:

- [Multi-stage builds](https://docs.docker.com/build/guide/multi-stage/):
-
    - To parallelize builds to increase speed.
-
    - To separate build and runtime stages to reduce final image size.
- [Effective cache utilization](https://docs.docker.com/build/cache/#optimizing-how-you-use-the-build-cache) to speed-up
  build times by:
-
    - Positioning expensive layers early.
-
    - Placing frequently changing layers last.
-
    - Keeping layers small (including only necessary files and dependencies).
-
    - Minimizing layer count.

Examples could be found in both, [standard](standard/Dockerfile) and [monorepo](monorepo/services/service_a/Dockerfile)
structures.

## CUDA Development Workbenches

This guide also covers how to build comprehensive CUDA environment workbenches, that can reliably build deep learning
frameworks, such as [PyTorch](https://github.com/pytorch/pytorch), from source. The same Dockerfile file can be found
in [standard](standard/workbench/Dockerfile) and [monorepo](monorepo/workbench/Dockerfile) structures.

## Standard Project Structure

For details on the standard project structure, refer to the [standard structure documentation](standard/README.md).

## Mono-Repository Structure

For details on the mono-repository structure, refer to
the [mono-repository structure documentation](monorepo/README.md).

## Workflows

### Starting a New Project

Follow these steps to start a new project:

```bash
pyenv install 3.12.3  # or the version you need
pyenv local 3.12.3
poetry init
... # Configure as needed
poetry install --no-root
```

### Installing an Existing Project

Follow these steps to install an existing project:

```bash
pyenv install 3.12.3  # or the version you need
pyenv local 3.12.3
poetry install
```

### Developing Locally

Follow these steps for local development:

```bash
poetry run ruff format  # format the files
poetry run ruff check --fix  # apply linting fixes 
poetry run python -m unittest discover
poetry run mypy .
```

### Building Docker Images

Follow these steps to build Docker images for services:

```bash
# Inside the service directory
export IMAGE_TAG=python-service-x
docker build -f Dockerfile -t $IMAGE_TAG .
```

### Running Docker Containers Locally

Follow these steps to run Docker containers locally:

```bash
# Be sure to have built the Docker image before
export IMAGE_TAG=python-service-x
docker run -p 8080:8080 --name local $IMAGE_TAG
```

### CI/CD

For details on CI/CD workflows, refer to the respective documentation:

- [Standard structure CI/CD workflows](standard/README.md#cicd-pipelines).
- [Mono-repository structure CI/CD workflows](monorepo/README.md#cicd-pipelines).
