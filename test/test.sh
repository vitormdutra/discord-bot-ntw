#!/bin/bash

GITPATH=/home/vitor/git
PROJECT=discord-bot-ntw

GIT=${GITPATH}/${PROJECT}

CTNR_NAME=discord-bot

cd ${GIT}

git pull

docker build -t ${PROJECT} .

docker stop ${CTNR_NAME}
docker rm ${CTNR_NAME}

docker run -d --restart=always --name ${CTNR_NAME} ${PROJECT}