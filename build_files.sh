python3 -m pip install -r requirements.txt
python3 manage.py migrate --noinput
python3 manage.py collectstatic --clear --noinput
python3 manage.py loaddata ladder/fixtures/ladders.json
