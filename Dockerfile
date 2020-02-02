FROM tiangolo/uwsgi-nginx-flask:python3.6
MAINTAINER Sander Puts

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
#RUN python -m spacy download en_core_web_lg
RUN wget "https://github.com/explosion/spacy-models/releases/download/en_core_web_lg-2.0.0/en_core_web_lg-2.0.0.tar.gz"
RUN pip install en_core_web_lg-2.0.0.tar.gz

COPY . / /app/
WORKDIR /app

COPY ./mordecai/serve.py /app/mordecai/serve.py

# debug only
RUN pip install flask

ENV OPTIONAL_ARGS=''
ENV PYTHONPATH "${PYTHONPATH}:/app"
ENV AM_I_IN_A_DOCKER_CONTAINER Yes

ENV LISTEN_PORT 8080
