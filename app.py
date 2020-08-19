import math


def is_prime(number):
    """
    This function  checks whether number is prime or not
    """
    if number <= 1:
        return False
    for i in range(2, (int)(math.sqrt(number)+1)):
        if number % i == 0:
            return False
    return True


def factorial(number):
    """
    This function returns factorial of a number
    """
    if number <= 1:
        return 1
    else:
        return number * factorial(number - 1)


def fibonacci(number):
    """
    This function returns sum of the previous two numbers
    """
    if number < 2:
        return number
    else:
        return fibonacci(number-1) + fibonacci(number-2)

    
    
print(is_prime(2))
print(factorial(5))
print(fibonacci(10))
