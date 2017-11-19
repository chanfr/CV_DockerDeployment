FROM ubuntu:16.04

MAINTAINER aflorido

#update apt listsm, packages and upgrade the system
RUN apt-get update && apt-get upgrade -y

#install python pip
RUN apt-get install -y python-pip

#install python packages
RUN pip install --upgrade pip
RUN pip install opencv-python --upgrade

#install opencv libraties
RUN apt-get install libopencv-dev -y

#create a new user called docker
RUN useradd -ms /bin/bash docker

# Set docker user by default
USER docker

# set /home/docker as working directory
WORKDIR /home/docker

#create devel folder
RUN mkdir devel

#copy the python script into /home/docker/devel
COPY applyOpencvProcess.py /home/docker/devel

#execute the python script if no other command is defined
CMD python devel/applyOpencvProcess.py