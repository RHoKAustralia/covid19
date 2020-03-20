FROM nginx:latest
ADD ./nginx/static.conf /etc/nginx/conf.d/nginx.conf
ADD ./static/ /usr/share/nginx/html/static/
EXPOSE 80
