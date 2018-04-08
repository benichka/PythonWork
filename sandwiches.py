def sandwichToppings(*toppings):
    print("The following toppings were added:")
    for topping in toppings:
        print(topping)

sandwichToppings("salmon")
print()
sandwichToppings("egg", "pepper")
print()
sandwichToppings("ham", "egg", "pepper")

