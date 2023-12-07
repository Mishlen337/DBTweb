FROM nginx

RUN apt-get update && apt-get install -y apache2-utils

COPY nginx.conf /etc/nginx/conf.d/default.conf
# COPY .htpasswd /etc/nginx/.htpasswd
# htpasswd -b -s nginx/.htpasswd radar
