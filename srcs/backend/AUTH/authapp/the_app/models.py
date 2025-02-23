from django.db import models
from django.contrib.auth.models import BaseUserManager

class user_creation(BaseUserManager):
    def create_user(self, email, password, **extra):
        email = self.normalize_email(email)
        res   = self.model(email=email, **extra)
        res.set_password(password)
        res.save(using=self._db)
        return res
    def create_superuser(self, email, password, **extra):
        raise "Create Super User Not Allowed Right Now!"

class usersModel(models.Model):
    firstname = models.CharField(max_length=50, null=False)
    lastname  = models.CharField(max_length=50, null=False)
    usermail  = models.EmailField(unique=True, null=False)
    password  = models.CharField(max_length=1000, null=False)
    activate  = models.BooleanField(default=False)
    USERNAME_FIELD  = 'usermail'
    REQUIRED_FIELDS = ['password']
    objects = user_creation()