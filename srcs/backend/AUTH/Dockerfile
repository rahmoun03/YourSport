FROM python
WORKDIR /work
RUN pip install --upgrade pip
RUN pip install django
RUN pip install django_rest_framework
COPY ./authapp .
CMD ["./start.sh"]