#!/bin/bash

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo "============================================"
echo "  Zyntro - AI Video Clipping Tool"
echo "============================================"
echo ""

if [ -n "${LLM:-}" ]; then
    case "$LLM" in
        google:*|google-gla:*|openai:*|anthropic:*|ollama:*)
            ;;
        *)
            echo -e "${YELLOW}Warning: Unsupported LLM value '$LLM'${NC}"
            ;;
    esac
fi

if docker compose version &> /dev/null; then
    DOCKER_COMPOSE="docker compose"
else
    DOCKER_COMPOSE="docker-compose"
fi

echo -e "${GREEN}Starting Zyntro...${NC}"
$DOCKER_COMPOSE up -d --build

echo ""
echo -e "${GREEN}Zyntro is starting up!${NC}"
echo "  - Frontend:  http://localhost:3107"
echo "  - Backend:   http://localhost:8000"
