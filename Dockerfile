FROM python:3.12

WORKDIR /app

ADD pdm.lock /app

RUN pip install pdm && pdm install

