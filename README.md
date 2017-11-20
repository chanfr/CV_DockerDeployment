# CV_DockerDeployment

Examples and documentatino of how to deploy a computer vision application. 

## Requirements for server execution using docker
### With gpu compatibility (only for ubuntu 16.04)
* Docker [Installation guide](https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/)
* Cuda:
```sh
    sudo apt-get install cuda
   ```
* nvidia-docker
```sh
    wget -P /tmp https://github.com/NVIDIA/nvidia-docker/releases/download/v1.0.1/nvidia-docker_1.0.1-1_amd64.deb
    sudo dpkg -i /tmp/nvidia-docker*.deb && rm /tmp/nvidia-docker*.deb
```

** Test nvidia-smi
```sh
nvidia-docker run --rm nvidia/cuda nvidia-smi
```

### Without gpu compatibility
* Docker [Installation guide](https://docs.docker.com/engine/installation)


## Requirements for client execution:
* Python 2 / 3
* OpenCV 3 for python
* Following python packages:
```sh
    pip install sklearn requests pillow --upgrade
```


## Aditional configuration
* Download the following docker images needed to execute the examples:
```sh
    docker pull chanfr/cv_dockerdeployment:server_gpu
    docker pull chanfr/cv_dockerdeployment:server_cpu
    docker pull chanfr/cv_dockerdeployment:python_opencv_example
```
* Include a user to docker group:

    In order to use docker with your own user, you have to include your user into the "docker" group:
sudo usermod -aG docker <USER>
