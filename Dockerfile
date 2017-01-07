FROM ubuntu:16.04
Maintainer Itamar Lavender <itamar.lavender@gmail.com>

RUN apt update && apt install -y \
  vim \
  lsb-release \
  python3.5 \
  python3-pip \
  python3-dev \
  libpq-dev \
  python3-cryptography


RUN mkdir /opt/sensudrive
ADD . /opt/sensudrive/
RUN pip3 install --upgrade pip
RUN export PYCURL_SSL_LIBRARY=nss; pip3 install -q --upgrade --exists-action=w -r /opt/sensudrive/requirements.txt
