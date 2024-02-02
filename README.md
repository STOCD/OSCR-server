# OSCR-django
django backend for OSCR

OSCR-django is a backend for [OSCR](https://github.com/STOCD/OSCR/tree/main) with the intent
of recording combat log data.

# Requirements
see requirements.txt

# Running
## Development
```bash
python3 -m venv ~/OSCR
source ~/OSCR/bin/activate

# Install OSCR
python3 -m pip install /<path_to_OSCR_repo>/.

# Install Requirements
python3 -m pip install -r requirements.txt

# Run
python3 manage.py runserver
```

## Production
TBD: Will provide a docker
