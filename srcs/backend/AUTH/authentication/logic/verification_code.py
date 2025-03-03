import random, string

def create_code():
    code  = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    tmplate = f'''
                            Good news mate 🎊!
                            Ready To Shine ✨?
        You're one step before joining the community of YourSport 🔥
        👉 Here is you verification code: {code}
        Do not share this code any one
        We can't wait to see you play you favorite sp⚽🏀🏐🏈🏉rt with our community
        Best Regard
        YourSport Team.
    '''
    return {'template': tmplate, 'code': code}