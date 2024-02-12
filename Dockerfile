FROM python:3.12.1-slim

COPY requirements-docker.txt /tmp/requirements-docker.txt
RUN python3 -m pip install -r /tmp/requirements-docker.txt

COPY requirements.txt /tmp/requirements.txt
RUN python3 -m pip install -r /tmp/requirements.txt

RUN rm -rf /tmp/*

COPY OSCR_django /opt/OSCR_django/
COPY docker/entrypoint.sh /opt/

WORKDIR /opt/OSCR_django/

EXPOSE 8000
ENTRYPOINT /opt/entrypoint.sh
