FROM ubuntu:latest

WORKDIR .

COPY . .

ENV HOST=google.com

RUN apt-get update -y
RUN apt-get install -y iputils-ping
RUN apt-get install -y python3 

CMD python3 mtu.py $HOST