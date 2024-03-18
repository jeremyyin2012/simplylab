FROM python:3.12
COPY sources.list /etc/apt/sources.list
COPY pip.conf /root/.pip/pip.conf

WORKDIR /app

ADD pdm.lock /app
ADD pyproject.toml /app
ADD .env /app
ADD simplylab /app

RUN pip install pdm && pdm install

