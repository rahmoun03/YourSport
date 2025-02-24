from rest_framework import status, response, views
from .serializers import auth_db_serial
from .models import auth_db


class sign_up(views.APIView):
    def post(req):
        serial = auth_db_serial(data=req.data)
        if serial.is_valid():
            serial.save()
            return response.Response(status=status.HTTP_201_CREATED)
        return response.Response(status=status.HTTP_400_BAD_REQUEST)