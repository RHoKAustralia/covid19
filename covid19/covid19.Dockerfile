FROM ubuntu:xenial-20200212

ENV PATH_APP=/app
ENV PATH_REQUIREMENTS=$(PATH_APP)/requirements

ADD ./ ./app

# REQUIREMENTS: APT
RUN apt-get update \
    && apt-get install -y \
    $(cat /app/requirements/apt.txt)

# REQUIREMENTS: PIP
RUN pip3 install -r /app/requirements/pip.txt

# PROJECT DIRECTORY
WORKDIR ${PATH_APP}

# INITIALISE DJANGO
RUN ./init-django.sh
RUN python3 /app/manage.py runserver 0.0.0.0:8000

# RUN DJANGO APP
ENTRYPOINT [ "bash" ]
EXPOSE 8000

