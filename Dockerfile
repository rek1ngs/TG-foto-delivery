FROM python:3.11-slim

WORKDIR /app

COPY . .
RUN apt-get update && apt-get install -y fonts-dejavu-core && rm -rf /var/lib/apt/lists/*
ENV PYTHONUNBUFFERED=1

CMD ["python", "Main.py"]