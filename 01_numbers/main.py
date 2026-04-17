


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

def main():

    print(add(3, 3))
    print(divide(9, 3))
    print(floor(5, 2))
    print(multiply(10, 10))
    print(square(8, 2))
    return 0

if __name__ == "__main__":
    main()