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

Constraint: expect that you will never see 2 police cars on 
a single block
'''
p = 2/10
n = 10
k = 7



"So far, at least 6 out of the more well known 11 Star Wars movies have been awful. If that trend continues, what is the probability that another 9 be awful?"
p = 6/11
n = 9
k = 9

# # or directly
# print((6/11)**9)


'''
Poisson

Five stray cats walk on your chicken coop every 2 hours at night. 
What is the probability that 9 stray cats walk on the coop in
3 hours on a given night?

Contraints: time of night, seasonality, other cats don't affect
this rate
'''
from math import e
def poisson_pmf(lmbda, k):
    return lmbda**k * e**(-lmbda) / factorial(k)


lmbda = 5 * 3/2
k = 9

# print(poisson_pmf(lmbda, k))


'''
When viewing a certain section of the sky at night, typically four shooting stars can be seen in a 30 minute period.  What is the probability of seeing seven shooting stars in 45 minutes?
'''
lmbda = 4 * 45/30
k = 7


'''
6 kids have funny ski crashes every hour on the bunny slope. What is the probability that during the 30 minutes you sit down to eat lunch and watch the bunny slope, you witness exactly 5 funny crashes. (no kids were harmed in the making of this example).
'''
lmbda = 6 * 1/2
k = 5


'''
in perseid meteor shower 2020 estimate the shooting 20 shooting star in an hour what is probablity that we will see a hundred shooting star from misnight to 6 am?
'''
lmbda = 20 * 6
k = 100


'''
you are riding you bike downtown. In any 10 blocks,
you realize that you have on average 2 blocks w police cars.
What is the probability that you see 7 blocks w police cars in the next 10 blocks?

Assume more than 1 police car can occur on a block
'''
lmbda = 2
k = 7


'''
On average, 25,539 cyclists cross the East River bridges every day . What is the probability that 200,000 cyclists will cross the East River bridges in a given week?
'''
lmbda = 25539 * 7
k = 200000




'''
On average, 4 runners run on the local track every 30 minutes during the day.
What is the probability that 15 runners run on the track
in any 2 hours during the day?
'''
lmbda = 4 * 4
k = 15


'''
"You eat an average of half a cup of fruit, three days out of the week.
What's the probability you'll eat two cups of fruit every day of the week?"

considering 7 days
    eat 1.5 cups of fruit out of 7 days

'''
lmbda = 1.5
k = 14



'''
So what are some good identifiers of when we should use which?  I.e. when we should use Binomial vs when we should use Poisson

Consider that Poisson events (successes) can occur nearly simultaneously, whereas Binomial events are discretized into unique moments/trials/observations
'''


'''
Random Vars and Coding Mathematical Formulations


'''

'''
Y is the result of rolling a 4-sided die, then a 7-sided die,
then a 12-sided die and processing it through this function:

y = (d4**3 + d7**2) * d12**(1/2)
'''
def roll_math(roll_lst):
    d4, d7, d12 = roll_lst
    return (d4**3 + d7**2) * d12**(1/2)


'''
What is the probability that:

P(Y <= 80) = ?

P(Y > 50) = ?
'''

''' Using Counting '''
outcomes_Y = []

for d4 in range(1, 4+1):
    for d7 in range(1, 7+1):
        for d12 in range(1, 12+1):
            outcomes_Y.append(roll_math([d4, d7, d12]))

for lst in outcomes_Y:
    print(lst)
