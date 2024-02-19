# OSCR-server
django backend for OSCR

OSCR-server is a backend for [OSCR](https://github.com/STOCD/OSCR/tree/main) with the intent
of recording combat log data.

There is a test server located at [kraust-oscr.koyeb.app](https://kraust-oscr.koyeb.app/swagger/)

# Requirements
see requirements.txt

# Running
## Development
```bash
python3 manage.py migrate
ENABLE_DEBUG=y python3 manage.py runserver
```

## Production

This Project should be deployable to cloud docker providers, however OSCR-server
is not currently production ready and needs to address its DB backend first.

- Currently we use the default sqlite provider which is not acceptable in cloud
deployments. In the future we will move to postgres.

- Logs may also be stored in DB instead of on the local FS.

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
