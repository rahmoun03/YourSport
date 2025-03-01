from .models import tokens_db
import string, random

def is_auth_user(access_token, refresh_token):
    try:
        user_data = tokens_db.objects.get(access_token=access_token)
        return user_data
    except:
        try:
            refresh = tokens_db.objects.get(refresh_token=refresh_token)
            refresh.access_token = ''.join(random.choices(
                string.ascii_uppercase + string.ascii_lowercase + string.digits, k=100))
            refresh.save()
            return refresh
        except:
            raise Exception("")