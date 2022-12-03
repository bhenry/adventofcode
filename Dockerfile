# syntax=docker/dockerfile:1

FROM python:3.11-slim-buster

WORKDIR /opt/app

RUN pip install advent-of-code-data

COPY . .

CMD ["python"]
