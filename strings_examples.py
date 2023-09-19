import math

def main():
    print('Bsu'.lower())
    print('bsu'.upper())
    print('welcome to bsu'.title())
    print('Welcome to BSU'.swapcase())
    print('Welcome to BSU'.capitalize())
    print('welcome 1#'.isalnum())
    print('Welcome 1'.isalpha())
    print('123'.isdigit())
    print('bsu1'.isdigit())
    print('123'.isdecimal())
    print('     BSU'.lstrip())
    welcome ="welcome to BSU"
    print(welcome.replace("BSU", "Prudue"))
    print('Welcome to BSU'.index("to"))
    print('Welcome to BSU'.find("to"))
    print(math.isnan(50))#isnan (is a number?)
    print(math.isnan(math.inf))#isnan (is a number?) inf is infinity
    print(math.factorial(5))
    print(math.fmod(10, 3))#10 divied by 3 of remainder
    numbers = [10,15,0,-10,10,10,7,5]
    print(numbers[1:5:2])
main()
