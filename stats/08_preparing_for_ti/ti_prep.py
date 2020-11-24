''' TI Style Questions (2020-11-23) '''

'''

TI Skills/Outline

* textbook problems re: Discrete Distrs and Probability
    * Recognize and solve problems related to:
        * Binomial
        * Poisson
        * Geometric
        * Uniform
        * Bayes Theorem

    
    * Understanding counting or binary through the lens of independent trials
        * binary ex: [0,1,1,0,1] <- each "coin flip or bit is independent of the other, if each bit is randomly generated"
        * trinary ex: [0, 1, 1, 2, 0]

    * Coding mathematical formulations

    * Analysis through Dictionaries
        * Pack values into dictionaries
            * Check membership vs not checking membership
        * Transform Dictionary values
        * General analytic approach
            * Create generative process
            * Load results into a dict
            * Interpret/Transform
'''

'''
Binomial Textbook Probs

You are sitting on a park bench watching city buses go by. On average,
two out of every 13 buses that goes by has an advertisement for
oat milk on it. What is the probability that, in one particular
set of observations, 10 out of 20 buses have oat milk ads on them?

p = 2/13
k = 10
n = 20

binomial_pmf(n, k, p)
'''

def factorial(n):
    prod = 1
    for num in range(1, n+1):
        prod *= num
    return prod

def combinations(n, k):
    return factorial(n) / (factorial(n-k) * factorial(k))

def binomial_pmf(n, k, p=0.5):
    return combinations(n, k) * (p**k) * ((1-p)**(n-k))


p = 2/13
k = 10
n = 20

# print(binomial_pmf(n, k, p))


'''
Write your own story problem to be solved with the binomial_pmf
'''

'''
On average 2 out of 7 plants have pest infestation , what is the probability that 5 out of 20 plants that I buy have pests.
'''
p = 2/7
n = 20
k = 5

# print(binomial_pmf(n, k, p))


'''
Christmas is coming up and sometimes Santa forgets to bring presents to your house. Out of the past 14 years he has only brought you presents 2 times. Given his track record what is the probability that he DOES remember to visit your house 6 out of the next 15 years?
'''
p = 2/14
n = 15
k = 6

# print(binomial_pmf(n, k, p))


'''
While walking down a street in New York City, you encounter five different pedestrians speaking a language other than english for every 20 people you pass. What is the probability you will encounter 13 people speaking a language other than english while walking past the next 45 pedestrians. 
'''
p = 5/20
n = 45
k = 13

# print(binomial_pmf(n, k, p))


'''
The train you take to work leaves on time 77% of the time.
What is the probability that your train will leave on time for work 15 out of 50 work days?
'''
p = 0.77
n = 50
k = 15


'''
On average in a group of butterfiles, 7 out of 10 have spots.  What is the probability that in a set of observations, two out of five have spots?
'''
p = 7/10
n = 5
k = 2

'''
Your favorite cafe sells coffee and tea as the beverages. The rate of purchase of these two items is equal. Assuming customers only buy one beverage, what is the probability that out of 100 customers 30 buy coffee?
'''
p = 0.5
k = 30
n = 100


'''
you are riding your bike downtown. In any 10 blocks,
you realize that you have on average 2 blocks w police cars.
What is the probability that you see 7 blocks w police cars in the next 10 blocks?
'''
p = 2/10
n = 10
k = 7



"So far, at least 6 out of the more well known 11 Star Wars movies have been awful. If that trend continues, what is the probability that another 9 be awful?"
p = 6/11
n = 9
k = 9

# or directly
print((6/11)**9)
#0.1228
