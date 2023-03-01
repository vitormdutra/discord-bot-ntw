FROM python:3.10

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN apt-get update
RUN apt-get install -y locales locales-all
RUN /usr/local/bin/python -m pip install --upgrade pip

ENV LC_ALL pt_BR.UTF-8
ENV LANG pt_BR.UTF-8
ENV LANGUAGE pt_BR.UTF-8
ENV PYTHONIOENCODING=utf-8
ENV TZ="America/Sao_Paulo"

RUN pip install --no-cache-dir -r requirements.txt
#RUN apt-get update && apt-get install -y ffmpeg
#RUN pip install --upgrade --pre yt-dlp

COPY . ./


CMD ["sh","-c","python3 spotif.py"]
