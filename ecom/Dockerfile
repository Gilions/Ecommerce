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
   
COPY poetry.lock pyproject.toml ./

RUN pip install "poetry==1.7.1" \
        && poetry config virtualenvs.create false \
        && poetry install --no-interaction --no-ansi

COPY ./src .
USER docker_admin

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]