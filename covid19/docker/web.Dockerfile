FROM python:3.6-alpine

ADD ./ ./app

# REQUIREMENTS: APT
RUN apk --no-cache add mariadb-dev gcc libc-dev

# REQUIREMENTS: PIP
RUN pip3 install -r /app/requirements/pip.txt

ENV DEBUG=False

# CLEAN UP: APT
RUN apk del libc-dev gcc

EXPOSE 8000

# PROJECT DIRECTORY
WORKDIR /app
