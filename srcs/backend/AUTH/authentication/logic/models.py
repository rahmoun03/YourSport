from django.db import models
from django.utils import timezone

class auth_db(models.Model):
    email = models.EmailField(unique=True, null=False, primary_key=True)
    password = models.CharField(max_length=10000, null=False)
    activation = models.BooleanField(default=False)

class tokens_db(models.Model):
    access_token = models.CharField(max_length=10000, unique=True)
    refresh_token = models.CharField(max_length=10000, unique=True)
    identity = models.EmailField(unique=True, null=False, primary_key=True)

class verificationSystem(models.Model):
    identity = models.EmailField(unique=True, null=False, primary_key=True)
    ActivationCode = models.CharField(max_length=8,null=False)

class informations(models.Model):
    identity = models.EmailField(unique=True, null=False, primary_key=True)
    username = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    age = models.IntegerField(null=False)
    create_at = models.DateField(default=timezone.now)
    favorite_game = models.CharField(max_length=50)
    team = models.CharField(max_length=50)