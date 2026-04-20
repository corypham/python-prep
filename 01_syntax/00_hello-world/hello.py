"""
Python is an intepreted language, meaning that it is all compiled and executed 
during runtime. It is dynamically typed as well, meaning variable types are checked
and determined at runtime rather than before compilation. Variables can also change
types during its lifetime of execution, allowing flexible and faster prototyping.
"""
def printWord():
    print("Hello World!")

print(type(5))

def main():
    printWord()
    return 0


"""
Every single python module/file has a built in variable called __name__ . 
Python always has one entry module, the file that the intepreter
starts executing first.

The if statement controls whether this file is being executed directly, not imported.
This allows the file to be ran as either a program or imported library without
duplicating boilerplate code.
"""

# // Every single python module/file contains a variable called __
if __name__ == "__main__":
    main()