FROM python:3.12

ADD . /app
WORKDIR /app

RUN pip install pipenv
RUN pipenv install --system

RUN useradd -ms /bin/bash qrapi
USER qrapi

ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:5000", "simple_api:create_app()"]
