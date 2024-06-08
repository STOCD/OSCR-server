#!/usr/bin/env sh
# This is the entrypoint into the django server.
# We perform automatic migrations which may not be desirable.

set -e

(
    python3 manage.py migrate --noinput
    python3 manage.py collectstatic --clear --noinput

    # Load the ladder information.
    python3 manage.py loaddata ladder/fixtures/*.json

    # Generate the ladder variants.
    python3 manage.py genladders

    gunicorn --workers ($(nproc) * 4) -t 0 --bind 0.0.0.0:8000 OSCR_django.wsgi:application
)
