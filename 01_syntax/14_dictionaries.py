# Dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates.

capitals = {"USA" : "Washington D.C",
            "India" : "New Dehli",
            "Russia" : "Moscow",
            "Poo" : 2
            }

# prints the value
print(capitals.get("USA"))
print(capitals.get("India"))
# prints None
print(capitals.get("kyla"))

# Update or add a new key value pair
capitals.update({"Germany":"Berlin"})
capitals.update({"USA":"Detroit"})

# remove/pop pair
capitals.pop("Russia")

# remove latest pair
capitals.popitem()

print(capitals)

# you can also directly access value by indexing key or get
print(capitals.get("USA"))

# returns all of the keys
keys = capitals.keys()

for key in capitals.keys():
  print(key)

# returns all the values in collection
values = capitals.values()

for value in values:
  print(value)

# items return a dictionary object with a 2d list of tuples
items = capitals.items()

# iterable unpacking / tuple unpacking
for key, value in capitals.items():
  print(f'key: {key}, Value: {value}')
# clear
capitals.clear()

print(capitals)

