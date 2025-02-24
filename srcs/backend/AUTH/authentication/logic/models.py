from django.db import models

class auth_db(models.Model):
    email = models.EmailField(unique=True, null=False)
    password = models.CharField(max_length=1000, null=False)
    activation = models.BooleanField(default=False)