import math
def basic_calculation():
    x = int(input("enter the x: "))
    y = int(input("enter the y: "))
    print("sum:", x + y)
    print("subtraction:", x - y)
    print("multiplication:", x * y)
    print("division:", x / y)
    print("modulus:", x % y)
    print("Exponentiation:", x ** y)
    print("Floor division:", x // y)

# Call the function once
basic_calculation()

def powerOfNumber():   # calculate the any numbers of any power
    n = int(input("enter the any number find the power: "))
    m = int(input("enter the power of the number: "))
    print(f"calculation of {m} power of {n} = {n ** m}")  

# Call the function
powerOfNumber()
