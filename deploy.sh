#!/usr/bin/env bash

python3 -m pip install -r requirements.txt

python3 manage.py migrate --noinput
python3 manage.py collectstatic --clear --noinput

# Load the ladder information.
python3 manage.py loaddata ladder/fixtures/ladders.json
