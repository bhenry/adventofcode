# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /opt/app

COPY . .

CMD [ "bash"]
