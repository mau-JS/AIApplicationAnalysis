"# NLPBasicAnalysis" 

1. Install docker

- Update the package index:
```
sudo apt-get update
```

- Install packages to allow apt to use a repository over HTTPS:
```
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common
```

- Add Docker’s official GPG key:
```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

- Set up the stable Docker repository:
```
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
```

- Update the package index again:
```
sudo apt-get update
```

- Install the latest version of Docker Engine and containerd:
```
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

- Docker should now be installed. You can verify the installation by running:
```
sudo docker --version
```

2. Run docker file

```
docker build -f Dockerfile . -t web-server-test
```

```
docker run --rm -it --name web-server-test -p 8000:80 web-server-test
```
