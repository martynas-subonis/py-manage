# py-manage

A personal, opinionated guide to managing Python projects. This guide originally recommended
using [pyenv](https://github.com/pyenv/pyenv), [pipx](https://github.com/pypa/pipx), and [poetry](https://github.com/python-poetry/poetry) for managing Python
projects. However, with the advent and continued development of [uv](https://github.com/astral-sh/uv), it is now the preferred tool.

Additional literature can be found below:

- ["Python Project Management Primer Revisited"](https://martynassubonis.substack.com/p/python-project-management-primer-a55).
- ["Python Project Management Primer"](https://martynassubonis.substack.com/p/python-project-management-primer).
- ["Optimizing Docker Images for Python Production Services"](https://martynassubonis.substack.com/p/optimizing-docker-images-for-python).

## Table of Contents

1. [Tooling](#tooling)
2. [Dockerfile Optimizations](#dockerfile-optimizations)
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

- Use [uv](https://github.com/astral-sh/uv) to manage Python versions, install and run tools in isolation, and handle project dependencies and packaging.
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

## Standard Project Structure

For details on the standard project structure, refer to the [standard structure documentation](standard/README.md).

## Mono-Repository Structure

For details on the mono-repository structure, refer to
the [mono-repository structure documentation](monorepo/README.md).

## Workflows

- [Installing Python](https://docs.astral.sh/uv/guides/install-python/).
- [Using tools](https://docs.astral.sh/uv/guides/tools/#using-tools).
- [Working on projects](https://docs.astral.sh/uv/guides/projects/).
- [Publishing a package](https://docs.astral.sh/uv/guides/publish/#publishing-a-package).
- [Using uv in Docker](https://docs.astral.sh/uv/guides/integration/docker/#using-uv-in-docker). 
- [Using uv in GitHub Actions](https://docs.astral.sh/uv/guides/integration/github/#using-uv-in-github-actions).

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
