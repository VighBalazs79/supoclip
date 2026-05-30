#!/bin/bash
cd backend
pip install uv
uv sync
uv run uvicorn src.main_refactored:app --host 0.0.0.0 --port ${PORT:-8000}
