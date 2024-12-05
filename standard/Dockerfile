FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS builder

WORKDIR /app

COPY pyproject.toml uv.lock README.md ./

RUN uv sync --frozen --no-group dev --no-install-project

FROM python:3.12.8-slim AS runtime

WORKDIR /app

ENV PATH="/app/.venv/bin:$PATH"

COPY src src
COPY main.py .

EXPOSE 8080

COPY --from=builder /app/.venv .venv

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
