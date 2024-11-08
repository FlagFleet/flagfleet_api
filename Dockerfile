FROM python:3.13

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir poetry && poetry install --no-root

CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]