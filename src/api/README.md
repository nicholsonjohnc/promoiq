## SSH into Webserver

ssh -i web_server_key_pair.pem ec2-user@ec2-35-153-198-209.compute-1.amazonaws.com

## Activate Virtual Environment

source venv/bin/activate

## Install Dependencies

pip install -r requirements.txt

## Run App

NOTE: Ensure proper host and port in main.py.

python app/main.py

## Build Docker Container

docker build -t promoiqbackend .

## Run App in Docker Locally

NOTE: Ensure proper host and port in main.py.

docker run -p 8080:80 -t promoiqbackend

## Run App in Docker on Webserver

NOTE: Ensure proper host and port in main.py.

docker run -d --restart=always -p 80:80 -t promoiqbackend











