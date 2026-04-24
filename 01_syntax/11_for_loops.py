# for loops = execute a block of code a fixed number of times
#             You can iterate over a range, string, sequence etc

# Counting to 10 by twos
for i in range(1, 11, 2):
    print(f"Count: {i}")

# Ranging through until a condition (pass or break)

for i in range(1, 21):
    if i == 13:
        break # or pass
    else:
        print(i)

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

#################################################################
# Countdown timer excercise
#################################################################
import time


def count_down():
    my_time = int(input("Enter the time in seconds: "))

    for i in range(my_time, 0, -1):
        seconds = i % 60
        minutes = int(i / 60) % 60
        hours = int(i / 3600)
        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        time.sleep(1)

    return None

def main():
    count_down()
    return 0

if __name__ == "__main__":
    main()