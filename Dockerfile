FROM python:3.12

ADD . /app
WORKDIR /app

RUN pip install pipenv
RUN pipenv install --system

ENTRYPOINT ["python", "run.py"]
