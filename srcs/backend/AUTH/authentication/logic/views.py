from rest_framework import status, response, decorators
from .serializers import auth_db_serial, tokens_db_serial
from .models import auth_db, tokens_db
import bcrypt
from .validat_pass import validate_passwd
from .get_token import generate_tokens
from .access_check import is_auth_user

@decorators.api_view(["POST"])
def register(req):
    serial = auth_db_serial(data=req.data)
    if serial.is_valid():
        password_status = validate_passwd(serial.validated_data['password'])
        if (password_status != 'Strong'):
            return response.Response({'Weak Password': password_status}, status=status.HTTP_400_BAD_REQUEST)
        hash_pass = bcrypt.hashpw(serial.validated_data['password'].encode('ASCII'), bcrypt.gensalt())
        serial.validated_data['password'] = hash_pass.decode('ASCII')
        tokens = generate_tokens(serial.validated_data['email'])
        tokens_serial = tokens_db_serial(data=tokens)
        #TODO Send Verefication's email 
        if tokens_serial.is_valid():
            tokens_serial.save()
        serial.save()
        return response.Response(status=status.HTTP_201_CREATED)
    return response.Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

@decorators.api_view(["POST"])
def login(req):
    try:
        email, password = req.data.get('email'), req.data.get('password').encode('ASCII')
        user = auth_db.objects.get(email=email)
    except:
        return response.Response({'error': 'Invalid Email'}, status=status.HTTP_404_NOT_FOUND)
    if bcrypt.checkpw(password, user.password.encode('ASCII')):
        user_tokens = tokens_db.objects.get(identity=email)
        return response.Response(
            {
                'active_user': user.activation,
                'Access-Token': user_tokens.access_token,
                'Refresh-Token': user_tokens.refresh_token
            }, status=status.HTTP_200_OK)
    return response.Response({'error': 'Invalid Password'}, status=status.HTTP_404_NOT_FOUND)

@decorators.api_view(['GET'])
def get_profile_data(req):
    print(req.headers)
    try:
        user_data = is_auth_user(req.headers.get('Access-Token'), req.headers.get('Refresh-Token'))
    except Exception as error:
        return response.Response({'Authentication': 'Permission Needed'}, status=status.HTTP_404_NOT_FOUND)
    infos = auth_db.objects.get(email=user_data.identity)
    res = {'email': infos.email, 'activation': infos.activation}
    return response.Response(res, status=status.HTTP_200_OK)