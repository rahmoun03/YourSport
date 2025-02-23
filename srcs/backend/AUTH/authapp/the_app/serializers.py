from rest_framework.serializers import ModelSerializer
from .models import user_creation

class creation_serializer(ModelSerializer):
    class Meta:
        model = user_creation
        fields = ["firstname", "lastname", "usermail", "password"]