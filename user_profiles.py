def build_profile(first, last, **user_info):
    """ Build a dictionary containing everything we know about a user. """
    """ Double star (**): tells Python to create an empty dictionary. """

    profile = {}
    profile['first name'] = first
    profile['last name'] = last
    for key, value in user_info.items():
        profile[key] = value

    return profile

user_profile = build_profile('albert', 'einstein',
                            location='princeton',
                            field='physics')

print(user_profile)
