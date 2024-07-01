# Using list and also making decision to it
# name that not in the list will get access denied
name = input("Enter a name that in the list: ")

if name in ['Bob', 'Tom', 'Mikes' ]:
    print('Access Granted')
else:
    print('Access Denied')