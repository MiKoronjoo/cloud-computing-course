#!/bin/bash

# Create a volume for client
sudo docker volume create clientvol

# Build the client image
sudo docker build -t client-image ./client

# Run the client container
sudo docker run --rm -it \
  --network mynetwork \
  -v clientvol:/clientdata \
  -e SERVER_HOST=server-container \
  -e SERVER_PORT=8000 \
  --name client-container \
  client-image
