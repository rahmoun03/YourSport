import string, random

def generate_tokens(email):
    access_token = ''.join(random.choices
                           (string.digits + string.ascii_uppercase + string.ascii_lowercase, k=100))
    refresh_token = ''.join(random.choices
                           (string.digits + string.ascii_uppercase + string.ascii_lowercase, k=100))
    return {'identity': email, 'access_token': access_token, 'refresh_token': refresh_token}