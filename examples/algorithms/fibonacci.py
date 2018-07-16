"This script is for calculating specific index of fibonacci sequence."

def fib(number):
    "Calculate specific index of fibonacci sequence based on given number."
    if number < 2: 
        return 1
    else: 
        return fib(number - 1) + fib(number - 2)