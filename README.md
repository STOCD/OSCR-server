# OSCR-server
django backend for OSCR

OSCR-server is a backend for [OSCR](https://github.com/STOCD/OSCR/tree/main) with the intent
of recording combat log data.

There is a test server located at [https://oscr-server.vercel.app/](https://oscr-server.vercel.app/)

# Requirements
see requirements.txt

# Running
## Development
```bash
ENABLE_DEBUG=y python3 manage.py migrate
ENABLE_DEBUG=y python3 manage.py runserver
```

## Production

# Serverless

This project has been tested to be deployable to [vercel](https://vercel.com) and includes
Support for both vercel's blob and postgres integrations.

# Docker Compose

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
python3 OSCR-django/manage.py generate_swagger -f yaml -u http://127.0.0.1 api-spec.yaml
```

# Creating an API Client

[Use openapi-generator-cli](https://github.com/OpenAPITools/openapi-generator-cli)

```bash
openapi-generator-cli generate -g python -o client -i api-spec.yaml \
    --additional-properties=packageName=OSCR_django_client,packageVersion=1.0.0
cd client && python3 -m twine upload dist/*
```
