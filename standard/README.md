# Standard Structure

The suggested structure for a standard Python project is:

```text
standard/
├── .gitignore
├── .python-version
├── .venv/
├── Dockerfile
├── LICENSE
├── main.py
├── pyproject.toml
├── README.md
├── uv.lock
├── src/
│   ├── __init__.py
│   ├── package_a/
│   │   ├── __init__.py
│   │   ├── module_x.py
│   │   └── ...
│   ├── package_b/
│   │   ├── __init__.py
│   │   ├── module_y.py
│   │   └── ...
│   └── ...
└── tests/
    ├── test_main.py
    ├── package_a/
    │   ├── __init__.py
    │   ├── test_module_x.py
    │   └── ...
    ├── package_b/
    │   ├── __init__.py
    │   ├── test_module_y.py
    │   └── ...
    └── ...
```

## Highlights

- **Dependency Management**: Use dependency groups correctly in `pyproject.toml`, avoiding inclusion of non-runtime
  dependencies when deploying the project to production.
- **Environment Isolation**: Ensure the project has its own isolated environment, including test runners and type
  checkers, defined as `dev` dependencies.
- **Organized Structure**: Maintain a clear directory structure separating source code, tests, and configuration files:
-
    - **Source Code**: All source code resides in the `src/` directory (except for the application entry point if
      needed, which in the above case is `main.py`).
-
    - **Tests**: All test code resides in the `tests/` directory, mirroring the source code structure for easy
      navigation.

The file layout here differs from the standard Python **packaging** structure. However, it allows for maintaining a
**standard deployable service structure** while also supporting the packaging of modules (if desired) in a standard
manner within the `.whl` distribution.

### CI/CD Pipelines

- [Code quality check workflow](../.github/workflows/standard_code_check.yaml).
- [Package building workflow](../.github/workflows/standard_package_build.yaml).
- [Docker image build workflow](../.github/workflows/standard_build_docker.yaml).
