FROM python:3.10-buster as builder

ARG SERVICE_NAME

ENV POETRY_VIRTUALENVS_CREATE true
ENV POETRY_VIRTUALENVS_IN_PROJECT true

WORKDIR /app
RUN pip install poetry==1.4.0 --quiet

COPY backend/${SERVICE_NAME}/ backend/${SERVICE_NAME}
COPY backend/* backend/
COPY makefile .



FROM builder as prod

ARG SERVICE_NAME

COPY poetry.lock .
COPY pyproject.toml .

RUN poetry install --with ${SERVICE_NAME}

EXPOSE 8000

ENV PYTHONPATH "${PYTHONPATH}:/app"

ENV SERV_NAME ${SERVICE_NAME}

# CMD ["poetry", "run", "uvicorn", "backend.${SERVICE_NAME}.main:app", "--reload"]
CMD ["make", "run_api", "SERVICE_NAME=${SERV_NAME}"]

