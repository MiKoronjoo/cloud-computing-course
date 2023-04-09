## Project Overview
This project contains two Docker containers - "server" and "client".
The server container runs a server application that creates a file with random text data and transfers it to the client.
The server container also provides REST API to insert, retrieve, and remove data.
The client container runs an application that connects to the server and performs the operations provided by the server.

## Prerequisites
To run this project, you need to have Docker installed on your system. You can download Docker from the [official website](https://www.docker.com/get-started/).

## Running the project
1. Clone this repository to your local machine.
```bash
git clone https://github.com/MiKoronjoo/cloud-computing-course.git
```
2. Change the working directory to the project
```bash
cd assignment2
```
3. Run the server script
```bash
chmod +x fileserver.sh
./fileserver.sh
```
4. Run the client script in another terminal
```bash
chmod +x fileclient.sh
./fileclient.sh
```
5. Once the containers are running, you can test the functionality by connecting to the client container shell using the following command:
```bash
chmod +x open_client_shell.sh
./open_client_shell.sh
```

## Cleaning up
To stop and remove the containers, run the following commands:
```bash
sudo docker stop server-container client-container mongo-container
sudo docker rm server-container client-container mongo-container
```
To remove the Docker images, run the following commands:
```bash
sudo docker rmi server-image client-image
```

## Conclusion
This project demonstrates how to create Docker containers for a server and client application.
The containers are connected to a user-defined network to allow communication between them.
The project also uses volumes to persist data between container restarts.
