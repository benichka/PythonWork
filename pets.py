def describe_pet(animal_type, pet_name):
    """ Display information about a pet. """
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# Simple call.
describe_pet("hamster", "harry")

# Named call.
describe_pet(pet_name="harry", animal_type="hamster")


# Default value for a function.
def describe_pet_bis(animal_type, pet_name='doggo'):
    """ Display information about a pet. """
    print("animal type: " + animal_type + "; name: " + pet_name)

describe_pet_bis("dog")
describe_pet_bis(animal_type="cat")
