FROM python:3.8-alpine

RUN apk add zlib-dev jpeg-dev gcc musl-dev xvfb

RUN pip install --upgrade pip;

WORKDIR /code
ADD . /code

RUN python -m pip install -U --force-reinstall pip

RUN pip install -r requirements.txt