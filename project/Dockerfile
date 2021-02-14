FROM python:3.8.5

ENV PYTHONUNBUFFERED 1

WORKDIR /code

ADD requirements.txt /code/

RUN pip install -r requirements.txt

ADD . /code/

EXPOSE 8000
