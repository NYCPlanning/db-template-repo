# [Choice] Python version: 3, 3.9, 3.8, 3.7, 3.6
ARG VARIANT="3.9"
FROM mcr.microsoft.com/devcontainers/python:0-${VARIANT}

ENV PYTHONUNBUFFERED 1

ENV POETRY_VERSION=1.3.2

# [Optional] If your requirements rarely change, uncomment this section to add them to the image.
# COPY requirements.txt /tmp/pip-tmp/
# RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
#    && rm -rf /tmp/pip-tmp

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>

RUN pip install "poetry==$POETRY_VERSION"

ENV PATH "$PATH:/root/.local/bin/"

COPY poetry.lock pyproject.toml ./

RUN poetry install --no-interaction --no-ansi

# Provide a known path for the virtual environment by creating a symlink
RUN ln -s $(poetry env info --path) /var/dev-poetry-venv

# Hide virtual env prompt
ENV VIRTUAL_ENV_DISABLE_PROMPT 1

# Start virtual env when bash starts
RUN echo 'source /var/dev-poetry-venv/bin/activate' >> ~/.bashrc