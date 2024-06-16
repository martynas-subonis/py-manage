# py-manage

A personal, opinionated guide to managing Python projects. A comprehensive writing and argumentation can be found
in ["Python Project Management Primer"](https://martynassubonis.substack.com/p/da065d88-e105-4040-86f9-6437da90e0e0).

## Table of Contents

1. [Tooling](#tooling)
2. [Mono-Repository Structure](#mono-repository-structure)
3. [Mono-Repository Structure Highlights](#mono-repository-structure-highlights)
4. [Flows](#flows)
    5. [Starting a New Project](#starting-a-new-project)
    6. [Installing an Existing Project](#installing-an-existing-project)
    7. [Developing Locally](#developing-locally)
    8. [CI/CD Pipeline](#cicd-pipeline)

## Tooling

- Use [pyenv](https://github.com/pyenv/pyenv) to manage `Python` versions.
- Use [pipx](https://github.com/pypa/pipx) to install and run global `Python` applications in isolated
  environments (`poetry` for example).
- Use [poetry](https://github.com/python-poetry/poetry) to manage `Python` dependencies and packaging.
- [minor] use [ruff](https://github.com/astral-sh/ruff) as a linter/formatter.

## Mono-Repository Structure

The suggested structure for Python mono-repositories is:

```
monorepo/
├── .gitignore
├── .python-version
├── .venv/
├── pyproject.toml
├── poetry.lock
├── poetry.toml
├── README.md
├── LICENSE
├── packages/
│   ├── package_a/
│   │   ├── .python-version
│   │   ├── .venv/
│   │   ├── pyproject.toml
│   │   ├── poetry.lock
│   │   ├── poetry.toml
│   │   ├── README.md
│   │   ├── LICENSE
│   │   ├── src/
│   │   │   └── package_a/
│   │   │       ├── __init__.py
│   │   │       ├── module_x.py
│   │   │       └── ...
│   │   └── tests/
│   │       ├── test_module_x.py
│   │       └── ...
│   └── package_b/
│       ├── .python-version
│       ├── .venv/
│       ├── pyproject.toml
│       ├── poetry.lock
│       ├── poetry.toml
│       ├── README.md
│       ├── LICENSE
│       ├── src/
│       │   └── package_b/
│       │       ├── __init__.py
│       │       ├── module_y.py
│       │       └── ...
│       └── tests/
│           ├── test_module_y.py
│           └── ...
│   └── ...
└── services/
    ├── service_a/
    │   ├── .python-version
    │   ├── .venv/
    │   ├── src/
    │   │   ├── __init__.py
    │   │   └── ...
    │   ├── Dockerfile
    │   ├── main.py
    │   ├── pyproject.toml
    │   ├── poetry.lock
    │   ├── poetry.toml
    │   └── tests/
    │       ├── test_main.py
    │       └── ...
    └── service_b/
        ├── .python-version
        ├── .venv/
        ├── src/
        │   ├── __init__.py
        │   └── ...
        ├── Dockerfile
        ├── main.py
        ├── pyproject.toml
        ├── poetry.lock
        ├── poetry.toml
        └── tests/
            ├── test_main.py
            └── ...
    └── ...
```

## Mono-Repository Structure Highlights

- Only specify tools that should be uniformly applied across the entire codebase, such as formatters and linters, at the
  root directory.
- Use dependency groups correctly, and do not include non-runtime dependencies when deploying services/packages to
  production/distribution.
- Organize services and packages into separate parent directories, as their CI/CD pipelines function differently:
-
    - Packages: The CI/CD pipeline builds and publishes their source and wheel archives.
-
    - Services: The CI/CD pipeline includes Docker build and publish steps, integration tests, and deployment stages.
- Ensure each package and service has its own isolated environment, including test runners and type checkers:
-
    - Include Python test runners as dev dependencies within each service/package. This allows you to open individual
      service/package folders as the project root in your IDE, enabling the IDE to recognize the test runners and
      facilitate test execution.
-
    - Provide exactly specified stubs for each package/service to ensure accurate type checking. Implementing a
      dedicated type check runner for each package/service simplifies this process and avoids the error-prone task of
      dynamically patching stubs with a single type check runner.
-
    - This approach provides flexibility to use different versions of test and type check runners, accommodating
      services that might not support the same versions.
-
    - This approach also makes it easy to parallelize CI pipelines, addressing the typically slow process of running
      tests and type checks during code quality checks.

## Flows

### Starting a New Project

```bash
pyenv install 3.12.3  # or the version you need
pyenv local 3.12.3
poetry init
... # Configure as needed
poetry install --no-root
```

### Installing an Existing Project

```bash
pyenv install 3.12.3  # or the version you need
pyenv local 3.12.3
poetry install --no-root
```

### Developing Locally

```bash
poetry run ruff format  # format the files
poetry run ruff check --fix  # apply linting fixes 
poetry run python -m unittest discover
poetry run mypy .
```

### CI/CD Pipeline

- [Linting and formatting workflow](.github/workflows/lint_format_check.yaml).
- [Parallelized testing and static typing workflow](.github/workflows/tests_static_typing.yaml).
- [Package building and publishing workflow](.github/workflows/build_dry_publish.yaml).