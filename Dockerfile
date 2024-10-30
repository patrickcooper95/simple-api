FROM python:3.12

ADD . /app
WORKDIR /app

# RUN pip install pipenv
# RUN pipenv install --system
RUN pip install flask
RUN pip install gunicorn

# ENTRYPOINT ["gunicorn", "-w", "4", "--bind", "0.0.0.0:5000", '"simple_api.create_app()"']
ENTRYPOINT ["python", "run.py"]
