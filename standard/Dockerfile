FROM python:3.12.4-slim AS builder

RUN pip install --upgrade pip==24.1.1 && \
    pip install poetry==1.8.3

WORKDIR /app

COPY pyproject.toml poetry.toml poetry.lock ./

RUN poetry install --only main

FROM python:3.12.4-slim AS runtime

WORKDIR /app

ENV PATH="/app/.venv/bin:$PATH"

COPY src src
COPY main.py .

EXPOSE 8080

COPY --from=builder /app/.venv .venv

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
