python3 -m pip install -r ./requirements.txt
python3 ./OSCR_django/manage.py migrate --noinput
python3 ./OSCR_django/manage.py collectstatic --clear --noinput
python3 ./OSCR_django/manage.py loaddata ladder/fixtures/ladders.json