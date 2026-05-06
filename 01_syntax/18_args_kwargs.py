#
# *args  = allows you to pass multiple non-key arguments into a tuple
# **kwargs = allows you to pass multiple keyword-arguments into a dict
#            * unpacking operator
#          1. positional 2. default 3. keyword 4. ARBITRARY
#

def add(a, b):
  return a + b

print(add(1, 2))

def new_add(*args):
  total = 0
  for arg in args:
    total += arg
  return total

print(new_add(1, 2, 3))

def display_name(*words):
  for word in words:
    print(word, end=' ')
    
print()
display_name("Dr", 'Spongebob', 'Harold', 'Squarepants', 2)

# use two unpacking operators 

def print_address(**kwargs):
  
  for key, value in kwargs.items():
    print(f'{key} : {value}')

print_address(street="23 Clear Creek", city='Irvine', state='CA')


# excercise

def shipping_label(*args, **kwargs):
  for arg in args:
    print(arg, end=' ')

  print()
  for key, value in kwargs.items():
    print(f'{key} : {value}')

  print(f"{kwargs.get('street')}")

  if 'pobox' in kwargs:
    print(f"{kwargs.get('pobox')}")

shipping_label("Dr.", "Spongebob", "III", 
               street="23 Clear Creek",
               apt="67",
               pobox='1001',
               city="Irvine",
               state="CA",
               zip="92620")