# iterate over items of any sequence (list or string)
words = ['cat', 'window', 'defenstrate']

for w in words:
    print(w, len(w))

# if you need to iterate over a sequence of numbers, use range() built in function
for i in range(6):
    print(i)

# start at another number and specify a different increment
print(list(range(2, 100, 20)))

# to iterate over indices of a sequence, combine range and len
a = ['Cory', 'Mary', 'Jeremy', 'John']
for i in range(len(a)):
    print(i, a[i])