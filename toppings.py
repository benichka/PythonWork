# Basic loop.
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for topping in requested_toppings:
    if(topping == 'green peppers'):
        print("Sorry, we're out of green pepper.")
    else:
        print("Adding " + topping + ".")

print("\nFinished making your pizza!")


# Checks if the list has at least one item in it.
print()
requested_toppings = []

if requested_toppings:
    for topping in requested_toppings:
        if(topping == 'green peppers'):
            print("Sorry, we're out of green pepper.")
        else:
            print("Adding " + topping + ".")
else:
    print("Are you sure you want a plain pizza?")

# Loop with check if an item is in a specific list.
print()
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for topping in requested_toppings:
    if(topping in available_toppings):
        print(topping + " was added to your pizza.")
    else:
        print("sorry, we don't have " + topping)

