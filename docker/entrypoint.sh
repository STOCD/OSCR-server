#!/usr/bin/env bash
# This is the entrypoint into the django server.
# We perform automatic migrations which may not be desirable.

(
    python3 manage.py migrate --noinput
    python3 manage.py collectstatic --clear --noinput

    gunicorn --workers $(nproc) -t 0 --bind 0.0.0.0:8000 OSCR_django.wsgi:application
)
