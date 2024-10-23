FROM python:3.12

ADD . /app
WORKDIR /app

RUN pip install pipenv
RUN pipenv install --system

ENTRYPOINT flask --app simple_api run -h 0.0.0.0
