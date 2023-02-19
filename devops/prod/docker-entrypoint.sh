#!/bin/sh

exec gunicorn -k uvicorn.workers.UvicornWorker -c /gunicorn_conf.py api.app:app