#
# module = a file containing code you want to include in your program
#          use 'import' to include a module (built in or your own)
#          useful to break up a large program into resusable sep files

# you can assign a module an alias
import math as m

# another way to import if you want a specific function
# from math import pi

a, b, c, d, e = 1, 2, 3, 4, 5
# to access the module
print(m.e ** a)

print(m.pi)

# import the py example module
import example as ex

print(ex.square(a))
print(ex.calc_circumference(e))
print(ex.area(b))

