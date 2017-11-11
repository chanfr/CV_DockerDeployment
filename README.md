# CV_DockerDeployment

Examples and documentatino of how to deploy a computer vision application. 


##Docker Installation (buntu 16.04)

sudo apt-get install apt-transport-https ca-certificates curl software-properties-common

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

sudo apt-get update

sudo apt-get install docker-ce



### Install nvidia-docker and nvidia-docker-plugin

wget -P /tmp https://github.com/NVIDIA/nvidia-docker/releases/download/v1.0.1/nvidia-docker_1.0.1-1_amd64.deb

sudo dpkg -i /tmp/nvidia-docker*.deb && rm /tmp/nvidia-docker*.deb

#### Test nvidia-smi
nvidia-docker run --rm nvidia/cuda nvidia-smi



In order to use docker with your own user, you have to include your user into the "docker" group:
sudo usermod -aG docker <USER>