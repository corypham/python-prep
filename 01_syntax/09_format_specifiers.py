"""
format specifiers = {value:flags} format a value based on what flags
                    are inserted

.(number)f = round to that many decimal places (fixed point)
:(number)  = allocate that many spaces
:03        = allocate and zero pad that many spaces
:<         = left justify
:>         = right justify
:^         = center align
:+         = use a plus sign to indicate positive value
:=         = place sign to leftmost position
:          = insert a place before positive nubers
:,         = comma separator
"""

price1 = 3.14123142
price2 = -987.65
price3 = 12.34
price4 = 123023808240708.2343423

# display up to two decimal places
print(f"Price 1 is ${price1:.2f}")

# allocate and pad 0 or spaces 
print(f"price 2 is ${price2:010}")

# left justify and allocate 10 spaces
print(f"price 3 is ${price3:<10}")

# add comma separators, precede with positive sign, round to nearest decimal
print(f"price 4 is ${price4:+,.2f}")