import random, string

save:list = []
for i in range(900000):
    toAdd:str =''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    if toAdd in save:
        print("===> Duplicated <===")
        break
    else:
        print('.', end='')
print('')