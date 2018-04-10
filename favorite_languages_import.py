from collections import OrderedDict

#favorite_languages = {
#        'Sara' : 'C',
#        'Jen' : 'Python',
#        'Ben' : 'C#',
#        'Jean-Claude' : 'Ruby',
#        'Jean-Louis' : 'C#',
#        }
favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(name + "'s favorite language is " + language + ".")

# Only for the keys:
print()
for k in favorite_languages.keys():
    print(k.title())

# It can be combined with other function:
print()
for k in sorted(favorite_languages.keys()):
    print(k.title())

# It also works with values:
print()
for v in favorite_languages.values():
    print(v.title())

# To avoid duplicate, we transform the list into a set:
print()
for v in set(favorite_languages.values()):
    print(v.title())

