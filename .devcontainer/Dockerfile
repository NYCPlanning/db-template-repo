# See here for image contents: https://github.com/devcontainers/images/tree/main/src/python

ARG VARIANT="3"
FROM mcr.microsoft.com/devcontainers/python:0-${VARIANT}

ENV PYTHONUNBUFFERED 1

ENV POETRY_VERSION=1.3.2

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

RUN pip install "poetry==$POETRY_VERSION"

ENV PATH "$PATH:/root/.local/bin/"

# COPY poetry.lock pyproject.toml ./
COPY pyproject.toml ./

RUN poetry install --no-interaction --no-ansi

# # Provide a known path for the virtual environment by creating a symlink
# RUN ln -s $(poetry env info --path) /var/dev-poetry-venv

# # Hide virtual env prompt
# ENV VIRTUAL_ENV_DISABLE_PROMPT 1

# # Start virtual env when bash starts
# RUN echo 'source /var/dev-poetry-venv/bin/activate' >> ~/.bashrc