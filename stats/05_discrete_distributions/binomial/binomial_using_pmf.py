def factorial(n):
    prod = 1

    for num in range(1, n+1):
        prod *= num

    return prod

def combinations(n, k):
    return int(factorial(n) / (factorial(n-k) * factorial(k)))

def binomial_pmf(n, k, p=0.5):
    return combinations(n, k) * (p**k) * (1-p)**(n-k)

# print(binomial_pmf(8, 4, p=0.5)) # 0.2734375


'''
What is the probability in 12 coin flips of a fair coin, that you get 7 heads?
'''
print(binomial_pmf(12, 7, p=0.5))

'''
"You have 14 components in a circuit. At any given time, there is a 95% chance that a given component is functioning. What is the probability that 12 components are functioning? Assume that each component functions independently of every other."
'''
print(binomial_pmf(14, 12, p=0.95))