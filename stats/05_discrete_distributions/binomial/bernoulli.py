from random import choice, random

'''
Random Variable
* results of some experiment
    * consider every potential outcome of an experiment
    * imagine running that experiment quasi-infinite number of times
        * should arrive at some set of parameters that define the distribution of the outcomes of that Random Variable
        * flip a coin an infinite - 1 number of times, if you divide the number of outcomes of Heads by infinite - 1, then you should have ~0.5
'''

'''
Consider a random variable Y.
    Y represents the outcome of a single roll of a 6-sided die
    Y = {1, 2, 3, 4, 5, 6}
What is the probability that Y has an even outcome?
0.5
'''

# roll a die
die_possibilities = [1,2,3,4,5,6]

Y_1 = choice(die_possibilities) # <- single experiment
Y_2 = choice(die_possibilities)
Y_3 = choice(die_possibilities)

# print(Y_1)
# print(Y_2)
# print(Y_3)

'''
X is a random variable that follows these rules:
X = 1 if the roll of a 6-sided die has an even count of pips
X = 0 if the roll of a 6-sided die has an odd count of pips
What is the P(X=0)?
0.5
'''
def get_X():
    if choice(die_possibilities) % 2 == 0:
        return 1
    else:
        return 0


'''
Consider a random variable Z.
Z is the result of summing the rolls of 1 6-sided die, 1 4-sided die, and 1 12-sided die.
What is the probability that Z is less than 10?
'''
def get_Z():
    outcomes = []

    for r1 in range(1,6+1):
        for r2 in range(1,4+1):
            for r3 in range(1,12+1):
                outcomes.append(sum([r1, r2, r3]))

    return outcomes

def analyze_Z():
    outcomes = get_Z()
    d = dict()

    for outcome in outcomes:
        if outcome not in d:
            d[outcome] = 0
        d[outcome] += 1
    
    return d

z_dict = analyze_Z()

# # display counts
# for k, v in sorted(z_dict.items()):
#     print(f'{k}: {v}')

# # display probas
# for k, v in sorted(z_dict.items()):
#     print(f'{k}: {v / sum(z_dict.values())}')

    

'''
Bernoulli trial (aka distribution)
single event with a binary outcome, with a set probability
If you have a coin that on average turns up heads in 90% of its flips, what is the probability that you'll get heads?
0.9
what is the probability that you'll get tails?
0.1
'''

def bernoulli(p_success=0.5):
    draw = random()
    
    if draw < p_success:
        return True
    else:
        return False

trials = 1000000
# print([bernoulli(p_success=0.5) for _ in range(trials)].count(True) / trials)


'''
A Binomial Distribution is a series of Bernoulli Trials, where we keep a fixed probability p.
How many ways can you arrange 1 1 in 5-bit binary?
00001
00010
00100
01000
10000
How many ways can you arrange 2 1s in 5-bit binary?
00011
00101
01001
10001
00110
01010
The Binomial Distribution Question:
If you have n Bernoulli trials in a row, what is the probability that k of them are successful?
You flip a coin 20 times. What is the probability that get 14 heads out of 20 flips?
0000001111111111111...
1111111100000000.....
...
'''



'''
How to count in Binary
consider decimal
00
01
02
03
..
09
10
11
12
..
99
00
no different for binary
0: 0000
1: 0001
2: 0010
3: 0011
4: 0100
5: 0101
6: 0110
7: 0111
8: 1000
9: 1001
10:1010
11:1011
12:1100
13:1101
14:1110
15:1111
can think a binary number as being a series of successes and failures
1 1 0 0
S S F F  -> 2 successes
The count of 1's in 4 bit-binary will follow a binomial distribution
0: *
1: ****
2: ******
3: ****
4: * 
0: 1/16
1: 4/16
2: 6/16
3: 4/16
4: 1/16
'''