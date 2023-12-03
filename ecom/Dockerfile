FROM python:3.11-alpine

RUN apk add --no-cache \
                    gcc \
                    curl \
                    libffi-dev \
                    musl-dev
WORKDIR /app

RUN addgroup -S web_ecom && adduser -S docker_admin -G web_ecom \
    && chown docker_admin:web_ecom -R /app
    
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
   
COPY ./ecom/poetry.lock ./ecom/pyproject.toml ./ecom/entrypoint.sh ./

RUN pip install "poetry==1.7.1" \
        && poetry config virtualenvs.create false \
        && poetry install --no-interaction --no-ansi

COPY ./ecom/src .
USER docker_admin

ENTRYPOINT ["./entrypoint.sh"]