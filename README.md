# Docker learning

<img width="405" alt="Screenshot 2024-11-12 at 19 51 13" src="https://github.com/user-attachments/assets/bcf2ca73-df0a-4ef8-8904-1379858c16c4">


## **Containers**

### **What are containers?**
- Lightweight, portable units for running applications 🐳  
- They bundle an application with all its dependencies, ensuring it runs consistently across different environments  
- Includes the code, runtime, libraries, and anything needed to run the application  

<img width="917" alt="Screenshot 2024-09-23 at 00 01 34" src="https://github.com/user-attachments/assets/033e038f-8bf4-44fc-b2d7-457742babc13">

### **Infrastructure**
- Represents the physical or virtual hardware where everything runs, e.g., your laptop  
 
### **Host Operating System**
- The operating system that runs directly on the infrastructure 🖥️  
- The foundation for everything above it (e.g. macOS)  

### **Docker Engine**
- What makes containerisation possible  
- Provides the environment to build, run, and manage containers  
- Without Docker Engine, containers won't run ⚙️  

---

### **Docker Containers**
- Holds an application and all its dependencies  
- Ensures each app runs consistently, regardless of the environment, and doesn't affect other containers  
- Lightweight and efficient since they share the Docker engine and host OS, but don't share internal information  

---

### **Benefits of Containers**
- **Isolation:** Ensures the application runs smoothly without interference, preventing conflicts  
- **Consistent environment:** Applications behave the same way across different deployments, ensuring reliability  
- **Efficiency:** More resource-efficient than virtual machines (VMs), as they share the host's kernel, reducing overhead and allowing more containers to run on the same hardware  

---

# Docker

---

## **What is Docker?**
- An open platform for developing, shipping, and running applications in containers  
- Simplifies container management, making it easier to build, deploy, and run apps 🚀  

---

### **Key Components of Docker**

### **Docker Engine**
- A portable, lightweight core service that runs and manages containers  

### **Docker Hub**
- A repository where you can find and share container images, like an app store for Docker images  

### **Images**
- Templates used to create containers  
- Like a snapshot of an application at a specific point in time, ensuring consistency as they are immutable  

### **Containers**
- Running instances of images that clients interact with  
- Can be started, stopped, and modified as needed  

### **Docker File**
- A file used to build Docker images  
- Contains a series of instructions that Docker uses to assemble an image  

---

## **Docker's Importance in Modern Development**

### Why is Docker so important?
Docker has revolutionised modern development due to several reasons:

### **Simplified deployment**
- Solves the issue of applications working inconsistently in different environments  
- Creates a consistent environment from development to production, eliminating the “it works on my machine” problem  

### **Improved Efficiency**
- Faster and more efficient than traditional virtual machines, as Docker is lightweight  
- Shares the system kernel, which speeds up processes  

### **Enhanced Collaboration**
- Makes it easy to share development environments with team members, ensuring consistency  
- Integrates smoothly with CI/CD pipelines, enabling automated testing and deployment  

---

# Containers vs VMs

---

## **What is the difference between containers and virtual machines?**

<img width="571" alt="Screenshot 2024-09-23 at 19 57 37" src="https://github.com/user-attachments/assets/92016d74-83d2-474c-92de-ca2ecdbb6fab">


### **Virtual Machines**
- Allows multiple operating systems to run on a single physical machine 🖥️  

### **Hypervisor**
- Responsible for creating and managing virtual machines, allocating resources like CPU, memory, and storage  

### **Guest OS**
- This is the guest operating system running on the virtual machine  
- Isolated from others and resource-heavy, consuming CPU, memory, and storage  

---

<img width="917" alt="Screenshot 2024-09-23 at 00 01 34" src="https://github.com/user-attachments/assets/dcb76775-fa22-4b07-b745-377b1fc4d8cc">

### **Containers**
- Lightweight compared to virtual machines  
- Share the host OS and use Docker Engine instead of a hypervisor  

### **Key Differences between Containers and VMs**

- **Startup time:** Containers start faster as they share the OS, while VMs take longer to boot up  
- **Resource usage:** Containers use fewer resources as they only require what's necessary, whereas VMs are more resource-heavy  
- **Isolation:** VMs provide stronger isolation since each has its own OS, while containers offer process-level isolation  
- **Portability:** Containers are more portable due to their lightweight nature, while VMs are less portable due to resource demands  

---

# Installing Docker on Mac

---

## **Step 1: Downloading Docker**
Visit the Docker website and download the appropriate version for your Mac (Silicon or Intel). 

<img width="1438" alt="Screenshot 2024-09-23 at 20 16 11" src="https://github.com/user-attachments/assets/05f6cbd1-13b4-4fe6-b34c-80916d704d80">


---

## **Step 2: Initialise**
Click on the `.dmg` file and drag it into the Applications folder.  

<img width="720" alt="Screenshot 2024-09-23 at 20 20 24" src="https://github.com/user-attachments/assets/f17dd757-d735-4c5c-a214-c93d9488f491">


---

## **Step 3: Create an Account**
Open the Docker app and sign up for an account.  

<img width="1277" alt="Screenshot 2024-09-23 at 20 24 36" src="https://github.com/user-attachments/assets/833df815-f8b7-4999-a742-b89552b7d574">

---

## **Step 4: Verify Installation**
Open Terminal and run the following command to check the installed version:

<img width="567" alt="Screenshot 2024-09-23 at 20 27 59" src="https://github.com/user-attachments/assets/0e7e15e7-9023-4468-a4ee-a1c531e015b7">

You should see the version of Docker installed. The second command provides an intense amount of information about docker that can be used for debugging.

---

## **Running a Simple Docker Container**
To test Docker, run the following command to execute a "Hello World" container:

<img width="567" alt="Screenshot 2024-09-23 at 20 35 47" src="https://github.com/user-attachments/assets/165be86f-58bd-4356-8c7f-d93cb51742b0">


### What happens when this command runs?
- **Pulls the image:** If the "hello-world" image isn't available locally, Docker pulls it from Docker Hub  
- **Creates a container:** Docker creates a new container from the image  
- **Runs the container:** The container runs a script that prints: "Hello from Docker!"  
- **Exits:** The container stops after printing the message  

---

# Docker Commands

---

| **Command**            | **Description**                                                                                     |
|------------------------|-----------------------------------------------------------------------------------------------------|
| `docker --version`      | Displays the installed version of Docker.                                                           |
| `docker info`           | Shows detailed info about the Docker installation and system status.                                |
| `docker run <image>`    | Creates and runs a new container from the specified image. Pulls the image if not found locally.     |
| `docker ps`             | Lists currently running Docker containers.                                                          |
| `docker ps -a`          | Lists **all** containers (running and stopped) on the system.                                       |

---

# Docker Images

---

## **What is a Docker File?**
- A series of instructions on how to build a Docker image  
- Each instruction creates a layer in the image, which makes it easy to track changes and optimise builds  
- Allows for repeatable builds, ensuring you can recreate the same environment every time  

---

## **Crucial Commands in a Docker File**

| **Command**   | **Description**                                                                 |
|---------------|---------------------------------------------------------------------------------|
| `FROM`        | Specifies the base image used to build your Docker image                         |
| `RUN`         | Executes commands in the container during the build process                      |
| `COPY`        | Copies files from the host machine into the container                            |
| `WORKDIR`     | Sets the working directory for instructions inside the container                 |
| `CMD`         | Specifies the command to run when the container starts                           |
| `EXPOSE`      | Informs Docker that the container listens on the specified port                  |

---

# **Example of a Docker File**

#<img width="840" alt="Screenshot 2024-09-23 at 19 32 13" src="https://github.com/user-attachments/assets/a3dadb8c-d070-413c-952a-b34259133450">



---

# Making a Simple Web Application

---

I created a simple web application using pre-built code from CoderCo and installed Python and Flask with:

```bash
pip3 install flask
```

### **What is Flask?**
Flask is a lightweight Python web framework ideal for building simple web apps and APIs. It’s easy to use, flexible, and perfect for small projects and prototypes.

The code was:

<img width="501" alt="Screenshot 2024-09-27 at 22 44 17" src="https://github.com/user-attachments/assets/6a42b79a-2af7-431e-adb3-03a6741f7dec">

Then I ran the web application by applying the command,

```bash
python3 app.py
```
<img width="494" alt="Screenshot 2024-09-26 at 19 45 34" src="https://github.com/user-attachments/assets/ea0c16b7-e7ca-4637-b9c9-2527d132d909">

The web site was running and it look like this:

<img width="826" alt="Screenshot 2024-09-26 at 19 46 32" src="https://github.com/user-attachments/assets/bf578742-95a4-4ebb-8c23-e1243bde8424">




---

## **Containerising My Web Application**

Here I containerised my web application. To do this I had to first make a docker file as a container will not process without a docker file. To first create docker file I used 

```bash
touch Dockerfile
```

Here I created my docker file.

<img width="497" alt="Screenshot 2024-09-26 at 23 05 20" src="https://github.com/user-attachments/assets/e3a6bdda-d085-4658-9574-e5155b81550a">

1:* Uses a lightweight Python 3.8 image as the base for the container.
2:* Sets the working directory inside the container to /app.
3:* Copies all files from your current directory to the /app directory in the container
4:* Installs the Flask package inside the container
5:* Indicates that the container will use port 5002 (used for documentation purposes)
6:* Specifies the command to run when the container starts, which launches the Flask app (app.py). 

Then I wanted to run the application on docker and i done this by doing,

docker build -t hello-flask 

docker build: This command tells Docker to build an image from a Dockerfile in the current directory.
-t hello-flask: The -t flag tags the image with the name
 hello-flask, making it easier to reference later.
.: The dot (.) at the end specifies the build context, indicating Docker should use the current directory (where the Dockerfile is located) to build the image

docker run -d -p 5002:5002 hello-flask

Here's a breakdown of the command `docker run -d -p 5002:5002 hello-flask`:

 **`docker run`**: This command starts a new container from a specified Docker image.
 **`-d`**: Runs the container in detached mode, meaning it runs in the background.
**`-p 5002:5002`**: Maps port 5002 on your host machine to port 5002 inside the container, making the Flask app accessible via `http://localhost:5002`.
**`hello-flask`**: The name of the Docker image to create the container from (built earlier using the `docker build` command).


---

# Command Table

---

| **Command**                      | **Description**                                                                                                 |
|-----------------------------------|-----------------------------------------------------------------------------------------------------------------|
| `docker --version`                | Displays the installed Docker version.                                                                          |
| `docker info`                     | Shows detailed information about the Docker installation and system status.                                      |
| `docker run <image>`              | Creates and runs a container from the specified image. Pulls the image if not available locally.                 |
| `docker ps`                       | Lists currently running Docker containers.                                                                      |
| `docker ps -a`                    | Lists all containers (running and stopped) on the system.                                                       |
| `docker build -t <name> .`        | Builds a Docker image from the Dockerfile in the current directory and tags it with the specified name.           |
| `docker run -d -p <host>:<cont> <image>` | Runs a container in detached mode (-d), maps host port to container port (-p), and specifies the image to use. |



# Docker Networking

Networking is crucial as containers need to communicate with each other efficiently and securely. 🌐

## Basic Networking Concepts in Docker

### **A Bridge Network**  
A default network mode for containers on the same machine.  
Containers contained in this network can communicate with each other using their own IP addresses.  
Isolated from the host machine network, which provides an extra layer of security.  

### **Host Network**  
The container uses the host machine's network directly without any isolation.  
Useful for applications that need to closely interact with the host system.  

### **None Network**  
Gives the container no network interface at all, which makes it completely isolated.  
Used when you want a container to have no network access whatsoever and can be useful for security scenarios. 🔒

In DevOps, Docker networking is important as it simplifies the implementation of **microservices** architecture.

### **Microservices**  
Allow different parts of an application to run as independent services, each in its own container.

## Linking Containers Together

The goal here was to link my recent Flask container to a MySQL database container. 

I started off by modifying my previous app using code from CoderCo and modifying my Dockerfile to ensure that it installs the MySQL database.

<img width="469" alt="Screenshot 2024-09-28 at 22 21 52" src="https://github.com/user-attachments/assets/e4cb6207-a8e5-44aa-bec8-65e9bba71837">


<img width="482" alt="Screenshot 2024-09-28 at 23 28 23" src="https://github.com/user-attachments/assets/c20d0ae0-19ce-41c2-903a-957bc73a0231">

### Breaking Down the Code

- **4**: A MySQL database was imported as this library enables us to execute SQL commands within our Python application.
- **11**: Setting the variable `db` to an instance that connects to my SQL database.
- **17**: A simple SQL query to fetch the MySQL version.
- **20**: What the website will display.

Then I created a custom network to allow my containers to communicate with each other using this custom network.

I ran the command to create my network:

```bash
docker network create my-custom-network  # Name of my network
```

Then I ran the command to run my SQL container:

```bash
docker run -d --name mydb --network my-custom-network -e MYSQL_ROOT_PASSWORD=my-secret-pw mysql:8
```

### Breaking Down the Code

This Docker command does the following:

- `docker run -d`: Runs a container in detached mode (in the background).
- `--name mydb`: Assigns the name `mydb` to the container.
- `--network my-custom-network`: Connects the container to the custom Docker network named `my-custom-network`.
- `-e MYSQL_ROOT_PASSWORD=my-secret-pw`: Sets the environment variable `MYSQL_ROOT_PASSWORD` inside the container to `my-secret-pw`, which is required to set the MySQL root password.
- `mysql:8`: Specifies the Docker image and version to use for the container (`mysql` image, version `8`).

Then I made sure to build the Docker image for the Flask app using the command:

```bash
docker build -t hello-flask-mysql . 
```

### Code Breakdown

- `docker build`: Initiates the build process for a Docker image.
- `-t hello-flask-mysql`: Tags the built image with the name `hello-flask-mysql`.
- `.`: Specifies the build context, indicating the current directory contains the Dockerfile and any other necessary files for the build.

Now to run my Flask application, I used the command:

```bash
docker run -d --name myapp5 --network my-custom-network -p 5002:5002 hello-flask-mysql
```

### Code Breakdown

- `docker run -d`: Runs the container in detached mode (in the background).
- `--name myapp5`: Names the container `myapp5`.
- `--network my-custom-network`: Connects the container to the Docker network named `my-custom-network`.
- `-p 5002:5002`: Maps port 5002 on the host to port 5002 inside the container, allowing external access to the application running on this port in the container.
- `hello-flask-mysql`: Specifies the Docker image to use for the container.

And finally, the output:

<img width="829" alt="Screenshot 2024-09-28 at 20 59 10" src="https://github.com/user-attachments/assets/8c6d0d4b-c704-449e-9cf9-8690aed8d791">



## Essential Docker Commands Used So Far in My Learning

| Command                                           | Description                                                                                                   |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| `docker images`                                   | Lists all Docker images on the system.                                                                        |
| `docker image ls`                                 | Lists all Docker images (alternative syntax).                                                                 |
| `docker rmi <image-id-or-name>`                   | Deletes a specific Docker image by its ID or name.                                                            |
| `docker rmi -f <image-id-or-name>`                | Force deletes a Docker image, even if it is being used by containers.                                         |
| `docker image prune`                              | Removes all unused *dangling* images.                                                                         |
| `docker image prune -a`                           | Removes all unused images (dangling and untagged).                                                            |
| `docker rm <container-id-or-name>`                | Deletes a specific stopped container by its ID or name.                                                       |
| `docker rm -f <container-id-or-name>`             | Force deletes a specific container, whether running or stopped.                                               |
| `docker container prune`                          | Removes all stopped containers.                                                                               |
| `docker ps`                                       | Lists all running containers.                                                                                 |
| `docker ps -a`                                    | Lists all containers, including stopped ones.                                                                 |
| `docker stop $(docker ps -q)`                     | Stops all running containers.                                                                                 |
| `docker rm $(docker ps -a -q)`                    | Deletes all containers (stopped and running, if forced).                                                      |
| `docker build -t hello-flask-mysql .`             | Builds a Docker image named `hello-flask-mysql` from the Dockerfile in the current directory.                 |
| `docker run -d --name myapp5 --network my-custom-network -p 5002:5002 hello-flask-mysql` | Runs a detached container named `myapp5` from the `hello-flask-mysql` image, connected to `my-custom-network`, with port 5002 exposed. |
| `docker login`                                    | Logs into Docker Hub or a private registry.                                                                  |
| `docker pull <image-name>`                        | Downloads a Docker image from a repository.                                                                   |

## Docker Compose

### What Is Docker Compose?  
A tool that allows you to define and manage multiple containers and Docker applications.  
Lets you define all your single files and manage them collectively.  
Acts as the organiser for your services, ensuring they work together smoothly. 🛠️

### What Does Docker Compose Do?  
It offers a powerful and efficient way to manage multiple container Docker applications.

### Key Features of Docker Compose

- **Docker-compose.yml File**: This file lists all the services your application needs (like a blueprint that describes each container).
- **Commands**: Due to Docker Compose simplicity, you can start, stop, and manage all your containers at once.
- **Networking**: Automatically creates a network for your containers.

### Importance of Docker Compose in DevOps

- Make development and testing easier.
- Ensures consistency.
- Enhances teamwork.

## My First Docker-compose.yml 

Firstly, I ensured that I made a Docker-compose.yml file using the `touch` command.

```bash
touch Docker-compose.yml
```

Then I tapped into the file and used this code.

<img width="525" alt="Screenshot 2024-10-02 at 00 32 15" src="https://github.com/user-attachments/assets/a0655535-e9e2-411a-96ca-5e205b14f36f">


### Code Breakdown

1. **Version `3.8`**: Specifies the Compose file format version.
2. **Services**:
   - **`web`**:
     - `build: .`: Builds the `web` service from the Dockerfile in the current directory (`.`).
     - `ports: "5002:5002"`: Maps port 5002 on the host to port 5002 inside the container, allowing external access.
     - `depends_on: mydb`: Ensures the `mydb` service starts before the `web` service.

   - **`mydb`**:
     - `image: mysql:8`: Uses the `mysql:8` image for the database service.
     - `environment`: Sets environment variables for the container:
       - `MYSQL_ROOT_PASSWORD: my-secret-pw`: Sets the root password for the MySQL database.

## Docker Registries

### What Is a Docker Registry?  
A storage and distribution hub for Docker images.  
Where your images live when they are not running as containers.  
**Key Features**: Public registries, Private registries.  

### Why Are Docker Registries Important in DevOps?  
Streamline deployment: Once images are stored, they can be easily accessed and deployed across multiple environments.  
Enhances collaboration: When images are stored in a centralised registry, everyone on the team has access to the same resources.  
Ensures consistency: By storing images, you can be sure that the exact same image is being used in deployment, testing, and production.

## Docker Hub

### What Is Docker Hub and What Is It Used For?  
- Docker Hub is a cloud-based repository for Docker images.  
- Stores pre-built images (public and private) for applications.  
- Allows sharing images with the community or specific teams.  
- Pull images from Docker Hub to run containers.  
- Push images to Docker Hub after building them locally.  
- Automated Builds: Automatically build images from GitHub/Bitbucket repos.  

In short, Docker Hub is where you store, share, and manage Docker images for easy container deployment. ☁️

| Command           | Description                            | Example                          | Purpose                         |
|-------------------|----------------------------------------|----------------------------------|---------------------------------|
| `docker push`     | Uploads a local image to a registry.    | `docker push user/repo:tag`      | Share/store image on registry.  |
| `docker pull`     | Downloads an image from a registry.

    | `docker pull user/repo:tag`      | Retrieve image to run locally.  |

- **`docker push`**: Upload images.  
- **`docker pull`**: Download images.


# AWS ECR

## What is AWS ECR and What Is It Used For?
AWS ECR (Elastic Container Registry) is a fully managed Docker registry service great for storing and managing private Docker images, especially when working within the AWS ecosystem. ☁️

## Putting AWS ECR Into Use

- Firstly I started by creating an ECR repository on the ECR console, ensuring it was private
- Then I named the repo ‘flask-mysql’ which was the same name as my docker image on docker hub
- After this I ensured to follow these steps on my terminal ensuring that I made sure it was perfect with no mistakes


Then I used the Docker command to link AWS with my container on the same network and ports.
<img width="521" alt="Screenshot 2024-10-01 at 22 48 30" src="https://github.com/user-attachments/assets/97ba9e5c-99dd-496e-a3cf-9d77a45d2123">


The application succeeded! 🎉

<img width="827" alt="Screenshot 2024-10-01 at 22 31 55" src="https://github.com/user-attachments/assets/bb60542e-e2a0-49d4-86b0-ce2d090054d0">

To save the process of creating a new network and aligning to protocols, I used the docker compose command following with the ECR.

<img width="521" alt="Screenshot 2024-10-01 at 23 54 22" src="https://github.com/user-attachments/assets/a83256a6-925e-4c38-9f74-45bb25e4d971">



## Important Docker Commands to Know!

| Command                                           | Description                                                  | Example                                      | Purpose                                        |
|---------------------------------------------------|--------------------------------------------------------------|----------------------------------------------|------------------------------------------------|
| `docker images`                                   | Lists all Docker images on the system.                       | `docker images`                              | View available images.                         |
| `docker inspect <image-id>`                       | Provides detailed information about an image.                | `docker inspect 12345`                       | Get detailed image info.                      |
| `docker rmi <image-id>`                           | Deletes a specific image by its ID.                          | `docker rmi 12345`                           | Remove an image.                              |
| `docker system prune`                             | Removes all unused objects like images, containers, networks.| `docker system prune`                        | Clean up unused Docker resources.             |
| `docker ps`                                       | Lists all running containers.                                | `docker ps`                                  | View active containers.                       |
| `docker ps -a`                                    | Lists all containers (running and stopped).                  | `docker ps -a`                               | View all containers (running/stopped).        |
| `docker stop <container-id>`                      | Stops a running container.                                   | `docker stop 67890`                          | Stop a container.                             |
| `docker rm <container-id>`                        | Deletes a stopped container completely.                      | `docker rm 67890`                            | Remove a container.                           |
| `docker container prune`                          | Removes all stopped containers.                              | `docker container prune`                     | Clean up unused containers.                   |
| `docker build -t <name> .`                        | Builds an image from a Dockerfile in the current directory.  | `docker build -t hello-flask-mysql .`        | Create an image from a Dockerfile.            |
| `docker run -d --name <name>`                     | Runs a container in detached mode (background).              | `docker run -d --name myapp5 myimage`        | Run containers in the background.             |
| `docker run -d --name myapp -p 5002:5002 <image>` | Runs a container, mapping ports and naming it.               | `docker run -d --name myapp5 -p 5002:5002 hello-flask-mysql` | Run a container with port mapping.            |
| `docker run -d --network <network-name>`          | Runs a container connected to a specific Docker network.      | `docker run -d --name myapp --network my-custom-network myimage` | Connect a container to a custom network.      |
| `docker pull <image-name>`                        | Downloads an image from Docker Hub or another registry.       | `docker pull mysql:8`                        | Fetch pre-built images from a registry.       |
| `docker push <image-name>`                        | Uploads a local image to a registry.                         | `docker push username/repository:tag`        | Share or store an image on Docker Hub.        |

---

## Making Our Image Lighter: Multistage Builds

### What Are Multistage Builds? 
Multistage builds allow you to use multiple `FROM` statements in your Dockerfile.  
You can use one `FROM` stage to build your application and another, much lighter stage to create the final image that you actually deploy.  

This approach lets you discard unnecessary files and dependencies, resulting in a much smaller, optimised image. This makes deployment faster and more efficient. 🚀

### Here Is a Multistage Build Put Into Action
I started with my original ‘my flask’ image.

First, I built the image using the command:
```bash
docker build -t my-flask-app:original
```
Using the `:original` tag to show the difference between the multistage and original image.  
Here, the image contained **688 MB**, which is quite large.  

<img width="525" alt="Screenshot 2024-10-02 at 00 23 36" src="https://github.com/user-attachments/assets/05e9f266-c492-4dd5-b8d3-f7d434a04f40">


Next, I edited my Dockerfile to meet the needs of the multistage image using the `FROM` command.

<img width="457" alt="Screenshot 2024-10-02 at 00 18 05" src="https://github.com/user-attachments/assets/74301b34-e880-43d0-958b-92d2943afe54">



Then I built the image by using the command:
```bash
docker build -t my-flask-app:multistage
```
Ensuring I differentiated it from the original image with the tag `:multistage`.  

Here, the image was much smaller in size.  

<img width="525" alt="Screenshot 2024-10-02 at 00 23 20" src="https://github.com/user-attachments/assets/0e87c01c-2fc0-45a8-b924-1a8e9637e6be">

I also edited my Docker Compose file to ensure that it met standards.

<img width="525" alt="Screenshot 2024-10-02 at 00 32 15" src="https://github.com/user-attachments/assets/6b60fd74-8898-43c1-b8aa-15826681899c">


And the application was successful! 🎉

---

## Kubernetes Introduction

### What Is Kubernetes?
Kubernetes is an open-source platform designed to automate the deployment, scaling, and operation of application containers.  
It takes container management to the next level by providing advanced features like container orchestration, automatic scaling, and self-healing. 

---

## Docker Swarm

### What Is Docker Swarm?
Docker Swarm is Docker's native clustering and orchestration tool, built into Docker.  
It is designed to be straightforward, making it a good choice for simpler or smaller deployments.

---

## Docker Swarm vs. Kubernetes

- **Auto Scaling**: Docker Swarm does not have built-in auto-scaling capabilities, meaning you need to manage scaling manually or through external tools.
- **Community Support**: Docker Swarm has a solid community that supports it.
- **Cluster Setup**: It's easier to start a cluster in Docker Swarm.

<img width="1319" alt="Screenshot 2024-10-02 at 00 46 35" src="https://github.com/user-attachments/assets/0349a94f-a4a8-46b1-8351-81e6cfa33dc7">


---

## Why Use Orchestration Tools?
- **Ensures Smooth Application Performance**: Helps applications run smoothly across different environments.
- **Manages Large-Scale Deployments**: Makes it easier to manage complex environments.
- **Ensures High Availability**: Automatically monitors the state of containers and can restart or relocate them in case of failure.
- **Automates Scaling and Recovery**: Can scale applications up or down based on demand, crucial for maintaining performance during peak times and saving resources during low usage periods.
- **Simple Deployment**: Streamlines the deployment process.
- **Enhances Reliability**: Increases the overall reliability of applications.
- **Resource Utilisation**: Ensures efficient use of resources.



