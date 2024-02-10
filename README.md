# OSCR-server
django backend for OSCR

OSCR-server is a backend for [OSCR](https://github.com/STOCD/OSCR/tree/main) with the intent
of recording combat log data.

# Requirements
see requirements.txt

# Running
## Development
```bash
python3 -m venv ~/OSCR
source ~/OSCR/bin/activate

# Install Requirements
python3 -m pip install -r requirements.txt

# Run
python3 OSCR-django/manage.py makemigrations user combatlog ladder
python3 OSCR-django/manage.py migrate
python3 OSCR-django/manage.py runserver
```

## Production
```bash
# Start up the server + proxy (add -d start up as a daemon)
docker compose up

# Create the superuser:
docker exec -it oscr-server python3 manage.py createsuperuser
```

# Generating the API Spec
```
python3 OSCR-django/manage.py generate_swagger -f yaml -u http://127.0.0.1 api-spec.yaml
```

# Creating an API Client
[Use openapi-generator-cli](https://github.com/OpenAPITools/openapi-generator-cli)
```
openapi-generator-cli generate -g python -o client -i api-spec.yaml \
    --additional-properties=packageName=OSCR_django_client,packageVersion=1.0.0
cd client && python3 -m twine upload dist/*
```
