from rest_framework import status, response, decorators
from .serializers import auth_db_serial
from .models import auth_db
import bcrypt

@decorators.api_view(["POST"])
def register(req):
    serial = auth_db_serial(data=req.data)
    if serial.is_valid():
        serial.validated_data['password'] = bcrypt.hashpw(serial.validated_data['password'].encode('ASCII'), bcrypt.gensalt())
        print(f"Password Stored on database {serial.validated_data['password']}")
        serial.save()
        return response.Response(status=status.HTTP_201_CREATED)
    return response.Response(status=status.HTTP_400_BAD_REQUEST)

@decorators.api_view(["POST"])
def login(req):
    email, password = req.data.get('email'), req.data.get('password').encode('ASCII')
    print(f"Email: {email}, Password: {password}")
    try:
        user = auth_db.objects.get(email=email)
    except:
        return response.Response({'error': 'Invalid Email'}, status=status.HTTP_404_NOT_FOUND)
    print(f"Hashed Pass Type: {type(user.password)}")
    if bcrypt.checkpw(password, user.password.encode('ASCII')):
        return response.Response(
            { 'active_user': False, 'access_token': "", 'refresh_token': ""}, status=status.HTTP_200_OK)
    return response.Response({'error': 'Invalid Password'}, status=status.HTTP_404_NOT_FOUND)
