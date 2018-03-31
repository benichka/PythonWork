motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'bmw'
print(motorcycles)

motorcycles.append('triumph')
print(motorcycles)

del motorcycles[1]
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

# Population with new data
motorcycles.append('kawasaki')
motorcycles.append('aprilia')
motorcycles.append('buell')
motorcycles.append('ducati')
motorcycles.append('harley-davidson')

popped_motorcycles = motorcycles.pop(1)
print(motorcycles)
print(popped_motorcycles)

# Remove by value
motorcycles.remove('ducati')
print(motorcycles)
