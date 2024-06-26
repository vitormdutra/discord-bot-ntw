FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    ffmpeg \
    libopus0

ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
ENV PYTHONIOENCODING=utf-8
ENV TZ="America/Sao_Paulo"
ENV DISCORD_TOKEN=''

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT python3 -m main -env=$DISCORD_TOKEN