def describe_pet(animal_type, pet_name):
    """ Display information about a pet. """
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# Simple call.
describe_pet("hamster", "harry")

# Named call.
describe_pet(pet_name="harry", animal_type="hamster")


# Default value for a function.
def simple_function(arg1, arg2='default value'):
    print("arg1: " + arg1 + "; arg2: " + arg2)

simple_function("toto")
