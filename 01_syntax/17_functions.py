# function = A block of reusable code
#            place () after the function to invoke it

# default arguments =  default value for certain parameters
#                      default is used when that arfument is omitted
#                      make your functions more flexible, reduces the # of
#                      arguments:
#                      1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary
def hello_world():
  print('Hello World')


hello_world()


def net_price(list_price, discount=0, tax=0.05):
  return list_price * (1 - discount) * (1 + tax)

print(net_price(500))

# make sure to place default arguments after positional arguments


# keyword arguments = an argument preceded by an identifier. helps with
#                     readability order of arguments dont matter:
#                     1. positional 2. default 3. KEYWORD 4. arbitrary


def hello(greeting, title, first, last):
  print(f'{greeting} {title}{first} {last}')

# you can mix up the order to positional arguments to set the parameters
hello("Hello", title="Mr.", last='Squarepants', first='Spongebob')