# builder stage

ARG PYTHON_VERSION=3.11

FROM python:${PYTHON_VERSION}-buster as builder

ARG POETRY_VERSION=1.6.1

RUN pip install poetry==${POETRY_VERSION}

WORKDIR /app

COPY . .

RUN poetry build --format wheel

# runtime stage

ARG PYTHON_VERSION=3.11

FROM python:${PYTHON_VERSION}-slim-buster as runtime

COPY --from=builder /app/dist/ .

RUN pip install /magic_combo-*.whl

ENTRYPOINT ["magic_combo"]
