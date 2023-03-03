# syntax=docker/dockerfile:latest
# See here for base image contents: https://github.com/devcontainers/images/tree/main/src/python
ARG VARIANT="3"
FROM mcr.microsoft.com/devcontainers/python:0-${VARIANT}

RUN export DEBIAN_FRONTEND=noninteractive

COPY . .
#  COPY bash/dev_build_setup.sh /opt/src/scripts/setup.sh
RUN bash/dev_build_env_setup.sh

# RUN bash/dev_install_python_packages.sh

# # Updating linux repo list and setting non interactive terminal
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive

# # Install postgresql client to use psql (postgresql alias)
# RUN apt-get -y install --no-install-recommends postgresql-client

# # Install minio for S3 file I/O
# RUN <<EOF
#     curl -O https://dl.min.io/client/mc/release/linux-amd64/mc
#     chmod +x mc
#     sudo mv ./mc /usr/bin
# EOF
