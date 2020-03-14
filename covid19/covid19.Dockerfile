FROM ubuntu:xenial-20200212

ENV PATH_APP=/app
ENV PATH_REQUIREMENTS=$(PATH_APP)/requirements

ADD ./ ./app

# REQUIREMENTS: APT
RUN apt-get update
RUN apt-get install -y \
    $(cat /app/requirements/apt.txt)

# REQUIREMENTS: PIP
RUN pip3 install -r /app/requirements/pip.txt 

EXPOSE 8000

