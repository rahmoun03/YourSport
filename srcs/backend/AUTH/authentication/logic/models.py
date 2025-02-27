from django.db import models

class auth_db(models.Model):
    email = models.EmailField(unique=True, null=False, primary_key=True)
    password = models.CharField(max_length=10000, null=False)
    activation = models.BooleanField(default=False)

class tokens_db(models.Model):
    access_token = models.CharField(max_length=10000, unique=True)
    refresh_token = models.CharField(max_length=10000, unique=True)
    identity = models.EmailField(unique=True, null=False, primary_key=True)