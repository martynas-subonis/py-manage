# Mono-Repository Structure

The suggested structure for Python mono-repository project is:

```text
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
│   │   ├── package_a/
|   │   │   ├── __init__.py
|   │   │   ├── module_x.py
|   │   │   └── ...
│   │   └── tests/
│   │       ├── __init__.py
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
│       ├── package_b/
|       │   ├── __init__.py
|       │   ├── module_y.py
|       │   └── ...
│       └── tests/
│           ├── __init__.py
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
    │       ├── __init__.py
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
            ├── __init__.py
            ├── test_main.py
            └── ...
    └── ...
```

## Highlights

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

### CI/CD Pipelines

- [Linting and Formatting Workflow](../.github/workflows/monorepo_lint_format_check.yaml).
- [Parallelized Testing and Static Typing Workflow](../.github/workflows/monorepo_tests_static_typing.yaml).
- [Package Building and Publishing Workflow](../.github/workflows/monorepo_build_dry_publish.yaml).