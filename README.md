# py-manage

A personal, opinionated guide to managing Python projects. A comprehensive writing and argumentation can be found
in ["Python Project Management Primer"]().

## Table of Contents

1. [Tooling](#tooling)
2. [Standard Project Structure](#standard-project-structure)
3. [Mono-Repository Structure](#mono-repository-structure)
4. [Workflows](#workflows)
    1. [Starting a New Project](#starting-a-new-project)
    2. [Installing an Existing Project](#installing-an-existing-project)
    3. [Developing Locally](#developing-locally)
    4. [CI/CD](#cicd)

## Tooling

- Use [pyenv](https://github.com/pyenv/pyenv) to manage `Python` versions.
- Use [pipx](https://github.com/pypa/pipx) to install and run global `Python` applications in isolated
  environments (`poetry` for example).
- Use [poetry](https://github.com/python-poetry/poetry) to manage `Python` dependencies and packaging.
- [minor] use [ruff](https://github.com/astral-sh/ruff) as a linter/formatter.

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

### CI/CD

For details on CI/CD workflows, refer to the respective documentation:

- [Standard structure CI/CD workflows](standard/README.md#cicd-pipelines).
- [Mono-repository structure CI/CD workflows](monorepo/README.md#cicd-pipelines).
