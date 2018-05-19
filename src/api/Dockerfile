# FROM ubuntu:16.04
# MAINTAINER John Nicholson "J.Nicholson.PhD@gmail.com"
# RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
#     DEBIAN_FRONTEND=noninteractive apt-get -y dist-upgrade && \
#     DEBIAN_FRONTEND=noninteractive apt-get -yq install net-tools nginx && \
#     useradd -ms /bin/bash nicholsonjohnc && \
#     rm -f /etc/nginx/fastcgi.conf /etc/nginx/fastcgi_params && \
#     rm -f /etc/nginx/snippets/fastcgi-php.conf /etc/nginx/snippets/snakeoil.conf
# EXPOSE 80
# EXPOSE 443
# COPY nginx/ssl /etc/nginx/ssl
# COPY nginx/snippets /etc/nginx/snippets
# COPY nginx/sites-available /etc/nginx/sites-available
# ENTRYPOINT ["/usr/sbin/nginx", "-g", "daemon off;"]




FROM tiangolo/uwsgi-nginx-flask:python3.6

# ENV LISTEN_PORT 443
# EXPOSE 443

RUN pip install --upgrade pip
RUN pip install Werkzeug
RUN pip install awscli --upgrade --user
RUN pip install boto3

COPY ./app /app


# FROM fedora:latest

# # Install miniconda.
# RUN yum -y update \
#     && yum -y install curl bzip2 \
#     && curl -ssl https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -o /tmp/miniconda.sh \
#     && bash /tmp/miniconda.sh -bfp /usr/local/ \
#     && rm -rf /tmp/miniconda.sh \
#     && conda install -y python=3.6 \
#     && conda update conda \
#     && conda clean --all --yes \
#     && rpm -e --nodeps curl bzip2 \
#     && yum clean all

# # Intall python packages.
# RUN conda install -c anaconda flask