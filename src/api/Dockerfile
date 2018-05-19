FROM tiangolo/uwsgi-nginx-flask:python3.6

ENV LISTEN_PORT 443
EXPOSE 443

RUN pip install --upgrade pip
RUN pip install Werkzeug
RUN pip install awscli --upgrade --user
RUN pip install boto3

COPY ./app /app