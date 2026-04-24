import math

####################################################################
# Basic arithmetic
####################################################################

friends = 5
friends += 1
friends -= 2
friends *= 3
friends /=2
friends *= 2

print(friends)

####################################################################
# Math Functions
####################################################################

x = 3.14
y = 4
z = 5

result = round(x)
result = abs(y)
result = pow(4, 3)
result = max(x, y, z)
result = min(x, y , z)

print(result)


####################################################################
# Math Module Import
####################################################################

print(math.pi)
print(math.e)
result = math.sqrt(9) 
result = math.ceil(x) # round a num up
result = math.floor(x) # round a num down

####################################################################
# Math Excercise
####################################################################

def calculate_radius():
  radius = float(input("Enter in the radius of a circle: "))
  area = math.pi * pow(radius, 2)
  print(f"The area of the circle is {area} cm^2")

  return None


####################################################################
# Math Functions
####################################################################

def add(a, b):
    return a + b

# returns a float
def divide(a, b):
    return a / b

# floor division: discards the fractional part
def floor(a, b):
    return a // b

def multiply(a, b):
    return a * b

def square(a, b):
    return a ** b

def modulus(a, b):
    return a % b

def main():

    print(add(3, 3))
    print(divide(9, 3))
    print(floor(5, 2))
    print(multiply(10, 10))
    print(square(8, 2))
    print(modulus(5, 2))
    calculate_radius()
    return 0

if __name__ == "__main__":
    main()