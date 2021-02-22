# Python basic
# Emil Parvanov
# 22/02/2021

def factorial(n):
    """ Number to calculate factorial"""
    if n < 1:
        b = -n
    else:
        b = n
    # The running total - eventually the factorial.
    total = 1
    # loop to do multiplications.
    while b > 1:
        total *= b
        b -= 1
    # Returning the answer
    if n < 1:
        return "Undentified"
    else:
        return total


n = 20
print(f"The factorial of {n} is {factorial(n)}")
