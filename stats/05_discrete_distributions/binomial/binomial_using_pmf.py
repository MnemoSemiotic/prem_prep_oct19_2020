def factorial(n):
    prod = 1

    for num in range(1, n+1):
        prod *= num

    return prod

def combinations(n, k):
    return int(factorial(n) / (factorial(n-k) * factorial(k)))

def binomial_pmf(n, k, p=0.5):
    pass