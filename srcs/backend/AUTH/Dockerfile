FROM python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /work
RUN pip install --upgrade pip
RUN pip install django
RUN pip install django_rest_framework
COPY ./authapp .
COPY ./deploy/run.sh .
RUN chmod +x run.sh
CMD ["./run.sh"]
