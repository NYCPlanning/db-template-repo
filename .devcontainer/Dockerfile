# syntax=docker/dockerfile:latest
# See here for base image contents: https://github.com/devcontainers/images/tree/main/src/python
ARG VARIANT="3.11"
FROM mcr.microsoft.com/devcontainers/python:0-${VARIANT}

RUN export DEBIAN_FRONTEND=noninteractive

COPY . .
#  COPY bash/dev_build_setup.sh /opt/src/scripts/dev_build_setup.sh
RUN bash/dev_build_env_setup.sh
