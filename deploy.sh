#!/usr/bin/env bash

python3 -m pip install -r requirements.txt

python3 OSCR_django/manage.py migrate --noinput
python3 OSCR_django/manage.py collectstatic --clear --noinput

# Load the ladder information.
python3 OSCR_django/manage.py loaddata OSCR_django/ladder/fixtures/ladders.json
