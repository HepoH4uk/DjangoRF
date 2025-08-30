FROM python:3.12-slim

WORKDIR /app

RUN apt-get update \
    && apt-get install -y gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY /requirements.txt /

RUN pip3 install -r /requirements.txt --no-cache-dir

COPY . .
