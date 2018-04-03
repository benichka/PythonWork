def build_person(first_name, last_name, age = ''):
    """ Return a dictionary of information about a person. """
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

musician2 = build_person('Jean-Claude', 'Dusse', '13')
print(musician2)
