# Jack Change It Online Card Game
This is an online card game built in Python using the Pygame framework. Additionally, the project leverages Flask as a web server. The application is Dockerized and it is setup for local deployment to Kubernetes.

## Prerequisites
`linux`
`pip`
`python3.12`
`docker`
`minikube`

### Setup
Here are steps to setup the project locally:

Install pip:

`sudo apt-get update`  

`sudo apt install pip`  

Install python3.12:  

`pip install python3.12`  

Install docker:  

<pre> # Add Docker's official GPG key: 
  sudo apt-get update 
  sudo apt-get install ca-certificates curl 
  sudo install -m 0755 -d /etc/apt/keyrings 
  sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc sudo chmod a+r /etc/apt/keyrings/docker.asc 
  
  # Add the repository to Apt sources: 
  echo \ "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \ $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \ sudo tee /etc/apt/sources.list.d/docker.list > /dev/null sudo apt-get update  
  sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
</pre>  

Verify docker engine installation:  

`sudo docker run hello-world`  

Install minikube (local k8s):  

`curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64`  
`sudo install minikube-linux-amd64 /usr/local/bin/minikube && rm minikube-linux-amd64`  

#### Next setup steps

Clone the repo to your linux machine, cd into the project directory and create a virtual environment using:  

`python3 -m venv env`  

Activate virtual env:  
`source env/bin/activate`  

Pull necessary dependencies from requirements.txt:  
`pip install -r requirements.txt`  


At this stage, the project can be started locally either by running main.py from the CLI, or running main.py from an IDE such as PyCharm:  

`python3 main.py`  

Addtionally, we can dockerize the application and run it as a container. First, if we want to run the container in k8s we need to ensure we are using minikubes docker daemon by doing:  

`eval $(minikube docker-env)`  

Otherwise we can skip that step.

Then we can dockerize the application using the follow commands from the project root:  

`docker build -t <name> .` where name can be whatever you would like to call it. I generally use jci for simplicity.  
`docker run -p 8000:5000 <name>` here we map port 8000 on the host to port 5000 within the container which is the standard port for the Flask web server.  

We can verify the container is running using:  
`docker ps`  

From here, we should be able to access the containerized application on:  
`localhost:8000`  

Finally, to run the application in k8s, we can use the following commands:  

`minikube start`  
`minikube kubectl -- get po -A` - this should prompt us to install the appropriate version of kubectl required to interact with the k8s cluster  
`kubectl apply -f deployment.yaml`  
`kubectl expose deployment <name> --type=NodePort --port=5000`  

From here we should be able to interact with the containerized application in the k8s cluster by doing the following:  
`minikube ip`  
`kubectl get services`  

Look for the k8s service that was created for your image name and there will be a cluster port associated in the range 30000-32767. These two network components constitute the socket for the application on the localhost. For example:  
`192.168.49.2:31789`  

Going to this address on the host machines web browser will allow us to access the game as a containerized application that is orchestrated by k8s.



   
