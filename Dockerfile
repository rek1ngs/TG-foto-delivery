FROM python:3.11-slim

WORKDIR /app

COPY . .
RUN apt-get update && apt-get install -y fonts-dejavu-core && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get install -y ttf-mscorefonts-installer
ENV PYTHONUNBUFFERED=1

CMD ["python", "Main.py"]