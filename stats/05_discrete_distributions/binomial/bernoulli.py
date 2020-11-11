from random import random

'''
Bernoulli Trial
'''

def bernoulli(p_success=0.5):
    draw = random()

    if draw < p_success:
        return True
    else:
        return False

# print(bernoulli(0.75))

'''
If you have a coin that on average turns up heads in 90% of its flips, what is the probability that you'll get heads?
0.9
'''

'''
A Binomial Process is a series of Bernoulli trials
where we keep a fixed probability p

The Binomials distr considers the sum of successes in a series of
Bernoulli trials

"Series of coin flips"
"Failures of multiples of the same component in parallel to each other"



"How many ways can you arrange 1 1-bit in 5-bit binary?"
00001
00010
00100
01000
10000

"How many ways can you arrange 2 1-bits in 5-bit binary?"
00011
00101
00110
01001
...

The Binomial Distr Question
If you have n Bernoulli trials in a row, what is the 
probability that k of them are successful?

You flip a coin 20 times. What is the proba that you
get 14 heads out of 20 flips?

You have 20 components in a parallel to each other. The
proba that any given component is functioning upon observation
is 0.5. What is the proba that 14 out of the 20 components is
functioning upon observation?

0000001111111111111111
0000010111111111111111
1000001111111111111110

'''


'''
How to count in binary?

'''