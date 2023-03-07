FROM python:3.10-slim-bullseye  as base

ARG UID=1000
ARG GID=1000

RUN apt-get update \
  && apt-get install -y --no-install-recommends build-essential curl libpq-dev \
  && rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man \
  && apt-get clean \
  && groupadd -g "${GID}" python \
  && mkdir -p /src \
  && useradd --create-home --no-log-init -u "${UID}" -g "${GID}" python \
  && chown python:python -R /src

ARG FLASK_ENV="production"
ENV FLASK_ENV="${FLASK_ENV}" \
    PYTHONUNBUFFERED="true"

WORKDIR /src

COPY --chown=python:python /src/app/requirements*.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=python:python src /src

EXPOSE 8000

CMD ["gunicorn", "-c", "python:app.config.gunicorn", "app.main:create_app()"]