#!/bin/bash

# Create a volume for server
sudo docker volume create servervol

# Create a user-defined network for the containers
sudo docker network create mynetwork

## Run the mongo container
sudo docker run --rm --network mynetwork --name mongo-container mongo:latest &

# Build the server image
sudo docker build -t server-image ./server

# Run the server container
sudo docker run --rm -it \
  --network mynetwork \
  -p 8000:8000 \
  -v servervol:/serverdata \
  --name server-container \
  server-image
