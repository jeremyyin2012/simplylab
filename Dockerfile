FROM python:3.12

RUN curl -sSL https://pdm-project.org/install-pdm.py | python3 -

WORKDIR /app

ADD pdm.lock /app

RUN pdm install

