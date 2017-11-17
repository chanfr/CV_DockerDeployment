FROM nvidia/cuda:8.0-cudnn6-devel

RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    aptitude locate\
    python python-pip python-setuptools libglib2.0-dev libsm-dev libxrender-dev libxext-dev

RUN updatedb
RUN pip install --upgrade pip


RUN git config --global http.sslVerify false
RUN mkdir -p /opt && \
    cd /opt && \
    git clone http://github.com/chanfr/CV_DockerDeployment

RUN pip install -r /opt/CV_DockerDeployment/requirements-gpu.txt

ENV PYTHONPATH=/opt/CV_DockerDeployment

EXPOSE 5000

WORKDIR /opt/CV_DockerDeployment/server

CMD python server.py --lenet=True