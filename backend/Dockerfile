FROM python:3.11-slim

RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*
RUN pip install uv

WORKDIR /app
COPY . .
RUN uv sync --no-cache

EXPOSE 8000
CMD uv run uvicorn src.main_refactored:app --host 0.0.0.0 --port ${PORT:-8000}

RUN pip install psycopg2-binary
