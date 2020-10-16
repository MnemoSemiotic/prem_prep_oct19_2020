from random import choice

def coin_flip():
    flip = ['H', 'T']
    return choice(flip)

# print(coin_flip())

'''
Write a function called series_of_flips, that has one parameter, n, which represents the number of coin flips. Return a list of the random coin flips.

['H', 'H', 'T', 'H']
'''
def series_of_flips(n):
    flips = []
    for _ in range(n):
        flips.append(coin_flip())
    return flips

# print(series_of_flips(4))

'''
Write a function called four_flip_sample_space that has no parameters. It should return a list of all possible outcomes for 4 coin flips.

[
    ['H', 'H', 'H', 'H'],
    ['H', 'H', 'H', 'T'],
    ['H', 'H', 'T', 'H']
    ...
    ['T', 'T', 'T', 'T']
]
'''
def four_flip_sample_space():
    flip = ['H', 'T']
    outcomes = []

    for f1 in flip:
        for f2 in flip:
            for f3 in flip:
                for f4 in flip:
                    outcomes.append([f1, f2, f3, f4])
    
    return outcomes


'''
What is the probability that in 4 coin flips, you get 3 heads?

A = THHH
    HTHH
    HHTH
    HHHT

S = len(outcomes)
'''

four_flips = four_flip_sample_space()

three_heads = []

for lst in four_flips:
    if lst.count('H') == 3:
        three_heads.append(lst)

# print(len(three_heads))
# print(len(four_flips))
# print(len(three_heads) / len(four_flips))



'''
What is in one coin flip, that you get a heads?
   P(H) = ?
T
H <--

In two coin flips, what is the P of getting both heads?
TT
TH
HT
HH <--

In three coin flips, what is the P of getting all heads?
TTT
TTH
THT
THH
HTT
HTH
HHT
HHH <--


Suppose you call the function series_of_flips(14). What is the probability that you 
will get all 'H' values?
(1/2)**14

What is the probability of getting this series of outcomes in 6 coin flips:
HTTHTH ?

(1/2)**6

What is the probability of getting 3 heads in 6 coin flips?
(need to either understand the cardinality of the subset and the superset OR, we use the binomial pmf)
'''


'''
In three six-sided dice rolls, what is the probability of getting a sum of the three rolls below 6?
'''

outcomes = []
for r1 in range(1, 6):
    for r2 in range(1, 6):
        for r3 in range(1, 6):
            outcomes.append([r1, r2, r3])

A = []

for rolls in outcomes:
    if sum(rolls) < 6:
        A.append(rolls)

# print(len(A) / len(outcomes)) # 0.08

'''
What is the probability of getting three 6's when rolling 3 6-sided dice?

(1/6)**3
'''



'''
Dependence:

What is the probability of choosing an ace of spades from a 52 card deck?
1/52

Given that the prior event has occurred, what is the P(Queen of Hearts)?
1/51
'''


'''
Multiplication Rule

If you have a series of independent events, say flipping a coin... you can calc a probability of that series of events occurring in a specific order by simply multiplying the probability of each event.

you flip a coin 7 times, what is the probability of getting 
HHTHTTT --> 0.5**7
'''


'''
Factorial intuition for space cardinality

If you have 5 people, and you have 5 chairs, how many different ways can you seat them in those chairs?

5!

a b c d e
a b c e d
a b d e c
'''

poss = ['a', 'b', 'c', 'd', 'e']
counts = []
arrangs = []

for p1 in poss:
    for p2 in poss:
        for p3 in poss:
            for p4 in poss:
                for p5 in poss:
                    counts.append([p1, p2, p3, p4, p5])
                    
for lst in counts:
    perm = True
    for item in lst:

        if lst.count(item) > 1:
            perm = False
    if perm:
        arrangs.append(lst)

# for item in arrangs:
#     print(item)

def factorial(n):
    prod = 1

    for num in range(1, n+1):
        prod *= num
    return prod

print(len(arrangs) == factorial(5))

['a', 'b', 'c', 'd', 'e']
['a', 'b', 'c', 'e', 'd']
['a', 'b', 'd', 'c', 'e']
['a', 'b', 'd', 'e', 'c']
['a', 'b', 'e', 'c', 'd']
['a', 'b', 'e', 'd', 'c']
['a', 'c', 'b', 'd', 'e']
['a', 'c', 'b', 'e', 'd']
['a', 'c', 'd', 'b', 'e']
['a', 'c', 'd', 'e', 'b']
['a', 'c', 'e', 'b', 'd']
['a', 'c', 'e', 'd', 'b']
['a', 'd', 'b', 'c', 'e']
['a', 'd', 'b', 'e', 'c']
['a', 'd', 'c', 'b', 'e']
['a', 'd', 'c', 'e', 'b']
['a', 'd', 'e', 'b', 'c']
['a', 'd', 'e', 'c', 'b']
['a', 'e', 'b', 'c', 'd']
['a', 'e', 'b', 'd', 'c']
['a', 'e', 'c', 'b', 'd']
['a', 'e', 'c', 'd', 'b']
['a', 'e', 'd', 'b', 'c']
['a', 'e', 'd', 'c', 'b']
['b', 'a', 'c', 'd', 'e']
['b', 'a', 'c', 'e', 'd']
['b', 'a', 'd', 'c', 'e']
['b', 'a', 'd', 'e', 'c']
['b', 'a', 'e', 'c', 'd']
['b', 'a', 'e', 'd', 'c']
['b', 'c', 'a', 'd', 'e']
['b', 'c', 'a', 'e', 'd']
['b', 'c', 'd', 'a', 'e']
['b', 'c', 'd', 'e', 'a']
['b', 'c', 'e', 'a', 'd']
['b', 'c', 'e', 'd', 'a']
['b', 'd', 'a', 'c', 'e']
['b', 'd', 'a', 'e', 'c']
['b', 'd', 'c', 'a', 'e']
['b', 'd', 'c', 'e', 'a']
['b', 'd', 'e', 'a', 'c']
['b', 'd', 'e', 'c', 'a']
['b', 'e', 'a', 'c', 'd']
['b', 'e', 'a', 'd', 'c']
['b', 'e', 'c', 'a', 'd']
['b', 'e', 'c', 'd', 'a']
['b', 'e', 'd', 'a', 'c']
['b', 'e', 'd', 'c', 'a']
['c', 'a', 'b', 'd', 'e']
['c', 'a', 'b', 'e', 'd']
['c', 'a', 'd', 'b', 'e']
['c', 'a', 'd', 'e', 'b']
['c', 'a', 'e', 'b', 'd']
['c', 'a', 'e', 'd', 'b']
['c', 'b', 'a', 'd', 'e']
['c', 'b', 'a', 'e', 'd']
['c', 'b', 'd', 'a', 'e']
['c', 'b', 'd', 'e', 'a']
['c', 'b', 'e', 'a', 'd']
['c', 'b', 'e', 'd', 'a']
['c', 'd', 'a', 'b', 'e']
['c', 'd', 'a', 'e', 'b']
['c', 'd', 'b', 'a', 'e']
['c', 'd', 'b', 'e', 'a']
['c', 'd', 'e', 'a', 'b']
['c', 'd', 'e', 'b', 'a']
['c', 'e', 'a', 'b', 'd']
['c', 'e', 'a', 'd', 'b']
['c', 'e', 'b', 'a', 'd']
['c', 'e', 'b', 'd', 'a']
['c', 'e', 'd', 'a', 'b']
['c', 'e', 'd', 'b', 'a']
['d', 'a', 'b', 'c', 'e']
['d', 'a', 'b', 'e', 'c']
['d', 'a', 'c', 'b', 'e']
['d', 'a', 'c', 'e', 'b']
['d', 'a', 'e', 'b', 'c']
['d', 'a', 'e', 'c', 'b']
['d', 'b', 'a', 'c', 'e']
['d', 'b', 'a', 'e', 'c']
['d', 'b', 'c', 'a', 'e']
['d', 'b', 'c', 'e', 'a']
['d', 'b', 'e', 'a', 'c']
['d', 'b', 'e', 'c', 'a']
['d', 'c', 'a', 'b', 'e']
['d', 'c', 'a', 'e', 'b']
['d', 'c', 'b', 'a', 'e']
['d', 'c', 'b', 'e', 'a']
['d', 'c', 'e', 'a', 'b']
['d', 'c', 'e', 'b', 'a']
['d', 'e', 'a', 'b', 'c']
['d', 'e', 'a', 'c', 'b']
['d', 'e', 'b', 'a', 'c']
['d', 'e', 'b', 'c', 'a']
['d', 'e', 'c', 'a', 'b']
['d', 'e', 'c', 'b', 'a']
['e', 'a', 'b', 'c', 'd']
['e', 'a', 'b', 'd', 'c']
['e', 'a', 'c', 'b', 'd']
['e', 'a', 'c', 'd', 'b']
['e', 'a', 'd', 'b', 'c']
['e', 'a', 'd', 'c', 'b']
['e', 'b', 'a', 'c', 'd']
['e', 'b', 'a', 'd', 'c']
['e', 'b', 'c', 'a', 'd']
['e', 'b', 'c', 'd', 'a']
['e', 'b', 'd', 'a', 'c']
['e', 'b', 'd', 'c', 'a']
['e', 'c', 'a', 'b', 'd']
['e', 'c', 'a', 'd', 'b']
['e', 'c', 'b', 'a', 'd']
['e', 'c', 'b', 'd', 'a']
['e', 'c', 'd', 'a', 'b']
['e', 'c', 'd', 'b', 'a']
['e', 'd', 'a', 'b', 'c']
['e', 'd', 'a', 'c', 'b']
['e', 'd', 'b', 'a', 'c']
['e', 'd', 'b', 'c', 'a']
['e', 'd', 'c', 'a', 'b']
['e', 'd', 'c', 'b', 'a']

'''
What is the probability, given the last question, that a and c are seated next to each other AND e and d are seated next to each other?
'''