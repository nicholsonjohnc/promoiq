## SSH into Webserver

```ssh -i web_server_key_pair.pem ec2-user@ec2-18-207-100-67.compute-1.amazonaws.com```

## Virtual Environment Setup

Create Virtual Environment

```virtualenv venv```

Activate Virtual Environment

```source venv/bin/activate```

Install Dependencies in Virtual Environment

```pip install -r requirements.txt```

## Run App

NOTE: Ensure proper host and port in main.py.

```python app/main.py```

## Build Docker Container

Do this everytime source changes!

```docker build -t promoiqbackend .```

## Run App in Docker Locally

NOTE: Ensure proper host and port in main.py.

```docker run -p 8080:80 -t promoiqbackend```

## Run App in Docker on Webserver

NOTE: Ensure proper host and port in main.py.

```docker run -d --restart=always -p 80:80 -t promoiqbackend```

docker run -p 80:80 -p 443:443 -v 











