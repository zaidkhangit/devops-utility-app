FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN apt-get update && apt-get  install -y  build-essential
RUN pip install --no-cache-dir -r requirements.txt --target /app/libraries
RUN rm -rf /var/lib/apt/lists/* && apt-get purge -y  build-essential
COPY . .
FROM gcr.io/distroless/python3-debian12 AS deployer
WORKDIR /app
COPY --from=builder /app /app
ENV PYTHONPATH="/app/libraries"
CMD ["uvicorn", "main:app", "--host", "0.0.0.0","--port","8081"]

