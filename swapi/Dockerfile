FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /requirements.txt


RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN pip install --upgrade pip
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev

RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

RUN apk update
RUN apk update \
    && apk --no-cache --update add build-base 
#RUN apk add make automake g++ subversion python3-dev build-essential manpages-dev

RUN pip install numpy==1.21.5
RUN pip install pandas


RUN mkdir /swapi
COPY ./swapi /swapi
WORKDIR /swapi
