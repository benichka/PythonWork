def make_car(make, modelName, **carInfos):
    car = {}
    car['make'] = make
    car['name'] = modelName

    for key, value in carInfos.items():
        car[key] = value

    return car

myCar = make_car('Renault', '19', color='white', isBreak=False)
print(myCar)
