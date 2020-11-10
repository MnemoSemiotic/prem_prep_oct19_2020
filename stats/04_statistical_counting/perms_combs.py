'''
Factorial
'''
def factorial(num):
    prod = 1
    for n in range(2, (num+1)):
        prod *= n
    return prod

print(factorial(5))