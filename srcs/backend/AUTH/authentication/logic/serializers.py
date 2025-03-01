from rest_framework.serializers import ModelSerializer
from .models import auth_db, tokens_db

class auth_db_serial(ModelSerializer):
    class Meta:
        model = auth_db
        fields = ['email', 'password']

class tokens_db_serial(ModelSerializer):
    class Meta:
        model = tokens_db
        fields = ['access_token', 'refresh_token', 'identity']