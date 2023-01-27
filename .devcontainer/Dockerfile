# See here for image contents: https://github.com/devcontainers/images/tree/main/src/python

ARG VARIANT="3"
FROM mcr.microsoft.com/devcontainers/python:0-${VARIANT}

# [Optional] If your requirements rarely change, uncomment this section to add them to the image.
# COPY requirements.txt /tmp/pip-tmp/
# RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
#    && rm -rf /tmp/pip-tmp

# Updating linux repo list and setting non interactive terminal 
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive 

# Install postgresql client to use psql (postgresql alias)
RUN apt-get -y install --no-install-recommends postgresql-client

#Install minio
RUN curl -O https://dl.min.io/client/mc/release/linux-amd64/mc\
    && chmod +x mc\
    && sudo mv ./mc /usr/bin
