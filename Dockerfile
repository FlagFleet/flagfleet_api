FROM python:3.13

WORKDIR /app

COPY poetry.lock pyproject.toml ./
RUN pip install --no-cache-dir poetry && poetry install --no-root

COPY . .

CMD ["poetry", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]