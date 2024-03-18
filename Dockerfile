FROM python:3.12

WORKDIR /app

ADD pdm.lock /app
ADD .env /app
ADD simplylab /app

RUN pip install pdm && pdm install

