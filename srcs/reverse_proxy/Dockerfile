FROM nginx
RUN apt update -y
COPY ./config/default.conf ./etc/nginx/conf.d
CMD [ "nginx", "-g", "daemon off;" ]