FROM python:3.9.17-bullseye


# copy files
COPY ./app/pyproject.toml /build/pyproject.toml
COPY ./app/poetry.lock /build/poetry.lock

# change working directory
WORKDIR /build

ENV PLAYWRIGHT_BROWSERS_PATH=/ms-playwright

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH "/root/.local/bin:${PATH}"

# Create Virtualenv
RUN python -m venv /opt/venv && \
  . /opt/venv/bin/activate && \
  pip install --no-cache-dir -U 'pip' && \
  poetry install --no-root --no-interaction --no-dev

WORKDIR /app/

COPY ./app /app

# make sure we use the virtualenv
ENV PATH="/opt/venv/bin:$PATH"

# add our app to the path
ENV PYTHONPATH="/app:$PYTHONPATH"
