FROM tiangolo/uwsgi-nginx-flask:python3.6

RUN pip install --upgrade pip
RUN pip install Werkzeug
RUN pip install awscli --upgrade --user
RUN pip install boto3
RUN pip install -U flask-cors

COPY ./app /app