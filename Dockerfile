FROM python:3.9.1
RUN apt-get update
ADD . /sho
WORKDIR /sho
RUN pip install --upgrade cython
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt