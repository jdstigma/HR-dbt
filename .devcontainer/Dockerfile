FROM mcr.microsoft.com/devcontainers/python:3.11

# Install PostgreSQL at build time
RUN apt-get update && \
    apt-get install -y postgresql postgresql-contrib && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies at build time
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
