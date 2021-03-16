FROM python:3.8

WORKDIR /app

ADD . /app

ENV export FLASK_ENV=development \
    export FLASK_app=app.py

RUN pip install -r requirements.txt 

CMD ["uwsgi", "app.ini"]
