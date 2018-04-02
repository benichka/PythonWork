favorite_languages = {
        'Sara' : ['C', 'C++'],
        'Jen' : ['Python', 'Ruby', 'Haskell'],
        'Ben' : ['C#', 'Java', 'Python'],
        'Jean-Claude' : ['Ruby'],
        'Jean-Louis' : ['C#', 'C++'],
        }

for name, languages in favorite_languages.items():
    print(name + "'s favorite languages are:")
    for language in languages:
        print("\t" + language)

