# OSCR-server
django backend for OSCR

OSCR-server is a backend for [OSCR](https://github.com/STOCD/OSCR/tree/main) with the intent
of recording combat log data.

# Requirements
see requirements.txt

# Generating Ladders

OSCR's base ladders are shipped as Django Fixtures, and additional ladder variants
need to be manually created by running a manage.py command.

```bash
python3 manage.py genladders
```

This process happens automatically when running docker compose.

# Running
## Development
```bash
ENABLE_DEBUG=y python3 manage.py migrate
ENABLE_DEBUG=y python3 manage.py runserver
```

## Production

### Docker Compose

Docker Compose streamlines running an instance of OSCR on a server. There is a sample
docker-compose.yaml file and to run OSCR all that needs to be typed is

```bash
docker compose up -d
```

Stopping OSCR can then be done with

```bash
docker compose down
```

# Create the superuser (for django admin):

```bash
python3 manage.py createsuperuser
```

# Generating the API Spec

API Specs are packaged along with our releases.


```bash
python3 manage.py generate_swagger -f yaml -u http://127.0.0.1 api-spec.yaml
```

# Creating an API Client

[Use openapi-generator-cli](https://github.com/OpenAPITools/openapi-generator-cli)

```bash
openapi-generator-cli generate -g python -o client -i api-spec.yaml \
    --additional-properties=packageName=OSCR_django_client,packageVersion=$(cat VERSION)
cd client
python3 -m build .
python3 -m twine upload dist/*
```
