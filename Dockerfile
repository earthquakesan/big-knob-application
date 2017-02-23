FROM ubuntu:16.04

MAINTAINER Ivan Ermilov <ivan.s.ermilov@gmail.com>

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y python3 python3-pip

RUN pip3 install --upgrade pip
RUN pip3 install django==1.10.5
RUN pip3 install gunicorn

COPY oneknob /oneknob
WORKDIR /oneknob

RUN mkdir -p /srv/logs/

EXPOSE 8000

COPY docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
