from rest_framework.serializers import ModelSerializer
from .models import auth_db

class auth_db_serial(ModelSerializer):
    class Meta:
        model = auth_db
        fields = ['email', 'password']