FROM ubuntu:18.04

RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    aptitude locate\
    python3 python3-pip python3-setuptools libglib2.0-dev libsm-dev libxrender-dev libxext-dev

RUN pip3 install --upgrade pip


RUN git config --global http.sslVerify false
RUN mkdir -p /opt && \
    cd /opt && \
    git clone http://github.com/chanfr/CV_DockerDeployment

RUN pip3 install -r /opt/CV_DockerDeployment/requirements.txt

ENV PYTHONPATH=/opt/CV_DockerDeployment

EXPOSE 5000

WORKDIR /opt/CV_DockerDeployment/server

CMD python3 server.py --lenet=True
