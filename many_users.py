users = {
        'aeinstein': {
            'first': 'albert',
            'last': 'einstein',
            'location': 'princeton',
            },
        'mcurie': {
            'first': 'marie',
            'last': 'curie',
            'location': 'paris',
            }
        }

for username, user_info in users.items():
    print("\nusername: " + username)
    full_name = user_info['first'].title() + " " + user_info['last'].title()
    location = user_info['location']

    print("\tFull name: " + full_name)
    print("\tlocation: " + location)
