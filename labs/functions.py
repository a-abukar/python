# Define the function
from unittest import result


def hello_user(name, age):
    print("Hello " + name + ", you are " + str(age))

# Calling the function
hello_user("Mike", 10)
hello_user("Steve", 30)

## Return 

def cube(num):
    return num*3

result = cube(3)
print(result)