FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install --no-cache-dir uv

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --dev

COPY src ./src
COPY tests ./tests
COPY benchmarks ./benchmarks
COPY demos ./demos
COPY AGENT.md README.md REPOSITORY_STRUCTURE.md ./

CMD ["uv", "run", "pytest"]
