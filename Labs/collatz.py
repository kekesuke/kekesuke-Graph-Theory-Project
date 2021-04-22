"""Verifying the Collatz conjecture."""
# Emil Parvanov
# 22.02.2021


def f(n):
    if n % 2 == 0:
        return n//2
    elif n % 2 == 1:
        return (3 * n) + 1


def collatz(n):
    so_far = []
    while n != 1:  # if n is not 1
        if n in so_far:  # if the number is already in the list to return true
            return True
        so_far.append(n)  # putting the number to the list
        n = f(n)  # storing the number from the collatz function
    so_far.append(n)  # appending the number to the list from the function
    return so_far  # returning the list after n is = 1


def prime(n):
    if n < 1:  # if n is less then 1 returning false
        return False
    for i in range(2, n):  # start from 2 ultil n
        if n % i == 0:  # checking if the remainder is 0 if the remainder is 0 that mean that the number can be devided by a number
            return False  # if remainder is 0 returning false

    return True


print(prime(9))
#print(f"collatz numbers: {collatz(27)}")
