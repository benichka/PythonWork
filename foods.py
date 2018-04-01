myFoods = ['pizza', 'falafel', 'carrot cake']

# To copy this list, just slice it with no boundaries
friendFoods = myFoods[:]

# CAREFUL: This also works, but it's not a copy: we are pointing to the same reference,
# so if friendFoods2 is modified, so is myFoods.
friendFoods2 = myFoods

print("My favorite foods are:")
print(myFoods)

print("\nMy friend's favorite foods are:")
print(friendFoods)

print("\nMy other friend's favorite foods are:")
print(friendFoods2)

# Let's append some foods and see how it goes.
myFoods.append('butter')
friendFoods.append('milk')

print("\nI have updated my favorite foods:")
print(myFoods)

print("\nMy friend updated his favorite foods:")
print(friendFoods)

print("\nWhat about my other friend?")
print(friendFoods2)

print("\nHere are my favorite foods")
for food in myFoods:
    print(food)
