FROM python:3.13.0-slim

COPY --from=ghcr.io/astral-sh/uv:0.5.11 /uv /uvx /bin/

ENV PYTHONUNBUFFERED=1

ENV UV_COMPILE_BYTE=1

ENV UV_LINK_MODE=copy
ENV PATH="/app/.venv/bin:$PATH"

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY ./pyproject.toml ./uv.lock ./.python-version /

# Install dependencies
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev


# Copy the project into the image
COPY . .

# Sync the project
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

# Expose the application port
EXPOSE 8083

# Run the FastAPI application using Uvicorn
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8083"]

CMD ["fastapi", "dev", "app/main.py", "--host", "0.0.0.0", "--port", "8083"]