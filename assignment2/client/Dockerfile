FROM ubuntu:latest

# Install required packages
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip

# Set working directory
WORKDIR /app

# Install Python dependencies
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

# Copy client code into container
COPY client.py .

# Start client application
CMD ["python3", "client.py", "server-container", "8000"]
