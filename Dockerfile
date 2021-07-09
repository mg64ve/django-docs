FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN apt-get update
RUN apt-get install -y default-mysql-client
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /code/
