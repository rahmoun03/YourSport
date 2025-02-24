from django.db import models

class auth_db(models.Model):
    email = models.EmailField(unique=True, null=False)
    password = models.CharField(unique=True, max_length=10000, null=False)
    activation = models.BooleanField(default=False)