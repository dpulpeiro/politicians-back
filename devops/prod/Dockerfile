FROM python:3.9-alpine3.16

# Use cached requirements if requeriments didn't changed
COPY devops/prod/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY src /app
COPY devops/prod/gunicorn_conf.py /gunicorn_conf.py
COPY devops/prod/docker-entrypoint.sh /docker-entrypoint.sh

RUN chmod +x /docker-entrypoint.sh && \
    addgroup -S appgroup && \
    adduser -S appuser -G appgroup

# Dont buffer python prints
ENV PYTHONUNBUFFERED=1

USER appuser
WORKDIR /app

ENTRYPOINT ["/docker-entrypoint.sh"]
