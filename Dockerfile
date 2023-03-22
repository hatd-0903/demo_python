FROM python:3.10.10

RUN apt-get update -qq

#init project
RUN mkdir /demo_python
WORKDIR /demo_python
ADD requirements.txt /demo_python/

RUN pip install -r requirements.txt
