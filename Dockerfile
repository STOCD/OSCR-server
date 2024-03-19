FROM python:3.12.1-alpine3.19

# Need to fetch the deps to build mysqlclient
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev

COPY requirements-docker.txt /tmp/requirements-docker.txt
RUN python3 -m pip install -r /tmp/requirements-docker.txt

COPY requirements.txt /tmp/requirements.txt
RUN python3 -m pip install -r /tmp/requirements.txt

RUN rm -rf /tmp/*
RUN apk del build-deps

EXPOSE 8000
ENTRYPOINT /opt/OSCR-server/entrypoint.sh
