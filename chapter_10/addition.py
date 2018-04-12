# Simple program to add two numbers, with exception handling.

print("Input 2 numbers and I'll add them.")
while (True):
    print("\nInput 'q' to exit.")
    number_1 = input("\nNumber 1: ")
    if (number_1 == 'q'):
        break
    try:
        number_1 = int(number_1)
    except ValueError:
        print("\nOnly number are accepted.")
        continue

    number_2 = input("\nNumber 2: ")
    if (number_2 == 'q'):
        break

    try:
        number_2 = int(number_2)
    except ValueError:
        print("\nOnly number are accepted.")
        continue

    try:
        result = number_1 + number_2
    except:
        print("\nError while adding " + number_1 + " and " + number_2 + ".")
    else:
        print(str(number_1) + " + " + str(number_2) + " = " + str(result))

