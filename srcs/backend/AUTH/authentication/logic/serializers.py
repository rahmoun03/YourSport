from rest_framework.serializers import ModelSerializer
from .models import auth_db, tokens_db, verificationSystem

class auth_db_serial(ModelSerializer):
    class Meta:
        model = auth_db
        fields = ['email', 'password']

class tokens_db_serial(ModelSerializer):
    class Meta:
        model = tokens_db
        fields = ['access_token', 'refresh_token', 'identity']

class verify_serializer(ModelSerializer):
    class Meta:
        model = verificationSystem
        fields = ['identity', 'ActivationCode']