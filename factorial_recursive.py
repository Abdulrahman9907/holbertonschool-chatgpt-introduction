#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
    Calculates the factorial of a given non-negative integer using recursion.
    The factorial of n (written as n!) is the product of all positive integers
    less than or equal to n. By definition, 0! = 1.
    
    Parameters:
    n (int): A non-negative integer for which to calculate the factorial
    
    Returns:
    int: The factorial of n (n!)
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Get the number from command line argument and calculate its factorial
f = factorial(int(sys.argv[1]))
print(f)
