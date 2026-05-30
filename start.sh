#!/bin/bash
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.cargo/bin:$PATH"
cd backend
uv sync
uv run uvicorn src.main_refactored:app --host 0.0.0.0 --port ${PORT:-8000}
