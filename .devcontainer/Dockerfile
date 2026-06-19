FROM mcr.microsoft.com/devcontainers/python:3.11

# Install PostgreSQL at build time
RUN apt-get update && \
    apt-get install -y postgresql postgresql-contrib pandoc texlive-xetex texlive-fonts-recommended texlive-plain-generic && \
    rm -rf /var/lib/apt/lists/*

# Grant vscode user passwordless sudo
RUN echo "vscode ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/nopasswd-vscode && \
    chmod 0440 /etc/sudoers.d/nopasswd-vscode

# Install Python dependencies at build time
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
