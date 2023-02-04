#!/bin/bash

GITPATH=/home/vitor/git
PROJECT=discord-bot-ntw

GIT=${GITPATH}/${PROJECT}

CTNR_NAME=discord-bot

cd ${GIT}

git pull

docker build -t ${PROJECT} .

docker stop ${PROJECT}
docker rm ${PROJECT}

docker run -d --restart=always --name ${CTNR_NAME} ${PROJECT}