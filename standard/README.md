# Standard Structure

The suggested structure for a standard Python project is:

```text
standard/
├── .gitignore
├── .python-version
├── .venv/
├── pyproject.toml
├── poetry.lock
├── poetry.toml
├── README.md
├── LICENSE
├── Dockerfile
├── main.py
├── workbench/  # Optional
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
- **Poetry Configuration**: To include multiple desired packages under the same distribution wheel while maintaining a
  structured directory, use configuration similar to:
  ```toml
  packages = [
    { include = "package_a", from = "src", to = "standard" },
    { include = "package_b", from = "src", to = "standard" }
  ]
  ```

The file layout here differs from the standard Python **packaging** structure. However, it allows for maintaining a
**standard deployable service structure** while also supporting the packaging of modules (if desired) in a standard
manner within the `.whl` distribution, thanks to the Poetry configuration.

### CI/CD Pipelines

- [Code quality check workflow](../.github/workflows/standard_code_check.yaml).
- [Package building and publishing workflow](../.github/workflows/standard_build_dry_publish.yaml).
- [Docker image build workflow](../.github/workflows/standard_build_docker.yaml).
