FROM ubuntu:latest

# Install required packages
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip

# Set working directory
WORKDIR /app

# Install Python dependencies
COPY ./requirements.txt .
RUN pip3 install -r ./requirements.txt

# Copy server code into container
COPY server.py .

# Expose server port
EXPOSE 8000

# Start server application
CMD ["python3", "server.py", "--port=8000"]
