from random import choice

def coin_flip():
    flip = ['H', 'T']
    return choice(flip)


'''
Write a function called series_of_flips, that has one parameter, n, which represents the number of coin flips. Return a list of the random coin flips.
if n=4, then something like this: ['H', 'H', 'T', 'H']
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
What is the probability that in 4 coin flips, you get exactly 3 heads?

A = THHH, HTHH, HHTH, HHHT

S = len(outcomes)
'''

four_flips = four_flip_sample_space()

# for outcome in four_flips:
#     print(outcome)

three_heads = []

for lst in four_flips:
    if lst.count('H') == 3:
        three_heads.append(lst)

# print(len(three_heads))
# print(len(four_flips))
# print(len(three_heads) / len(four_flips))


'''
Suppose you call the function series_of_flips(14). 
What is the probability that you get all 'H' values?

HHHHHHHHHHHHHH <--
HHHHHHHHHHHHHT
HHHHHHHHHHHHTH
HHHHHHHHHHHHTT
...

first consider the probability of P(H) for one flip
0.5

H <--
T

next consider P(HH) for two flips
0.25

HH <--
HT
TH
TT

... P(HHH) ...
0.125 = 0.5*0.5*0.5


P(H 14 times) = (1 / 2)**14
'''


'''
Suppose you call the function series_of_flips(14). 
What is the probability that you get at least one 'T' value?

P(at least one T in 14 flips) = 1 - (1 / 2)**14
'''


'''
Suppose you call the function series_of_flips(14). 
What is the probability that you get 5 'T' values?
We don't yet have the best tools to answer this

HHHHHHHHHTTTTT
HHHHHHHHTHTTTT
HHHHHHHTHHTTTT

Binomial Distribution (we'll learn this later)
'''

'''
What is the probability of getting this exact series in 6 coin flips:
HTTHTH?

0.5**6

NOTE: A very different question would be:
What is the probability of getting exactly 3 tails in 6 coin flips?
could use nested for loops, or binomial pmf
'''



'''
In three six-sided dice rolls, what is the P of getting a sum of the three rolls below 6?
'''
outcomes_S = []

for r1 in range(1, 6+1):
    for r2 in range(1, 6+1):
        for r3 in range(1, 6+1):
            outcomes_S.append([r1, r2, r3])

A = []

for roll in outcomes_S:
    if sum(roll) < 6:
        A.append(roll)

# print(len(A) / len(outcomes_S)) # ~0.0463



'''
Multiplication Rule example

What is the probability of getting 3 6's when rolling 3 6-sided dice?
(1/6)**3

111
112
113
114
115
116
121
122
123
'''


'''
In a probabilistic process, you roll 1 6 sided-die, flip a coin, then roll a 12-sided die.

What is the probability that you'll get this exact sequence:
2, Heads, 7 ?

1/6 * 1/2 * 1/12

What is the probability that you'll get:
< 3, Tails, > 6 ?

2/6 * 1/2 * 6/12
'''



'''
Dependence

What is the probability of choosing an ace of spades from a 52 card deck, without replacement?
1/52

Given that the prior event has occurred, what is the P(Queen)?
4/51


What is the probability of choosing an ace of spades from a 52 card deck and then
choosing a queen?
1/52 * 4/51
'''


'''
Another Mult Rule Example

The probability of catching a taxi on a busy street within 5 mins is 0.25
The probability of seeing a bluebird while in the taxi is 0.03
The probability that the mail has arrived when you get home is 0.78

What is the probability that all these events will occur?
0.25 * 0.03 * 0.78

Independent events are "Mutually Exclusive" events
'''

