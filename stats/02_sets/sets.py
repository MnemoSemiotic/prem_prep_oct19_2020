

'''
Random Experiments
'''

from random import choice

def coin_flip():
    flip = choice(['H', 'T'])
    return flip

# 20 flips
twenty_flips = []

for _ in range(20):
    twenty_flips.append(coin_flip())

# print(twenty_flips.count('H'))
# print(twenty_flips.count('T'))


def die_roll(sides=6):
    return choice(range(1, sides+1))

# sum of 20 die rolls
twenty_rolls = []
for _ in range(20):
    twenty_rolls.append(die_roll())

# print(sum(twenty_rolls))


'''
For the moment, consider the set() type in python to be a way to remove duplicates
from lists
'''

# list/set trick for deduping (doesn't maintain order)
# s1 = list(set([7,8,9,0,1,2,3,4,7,8,9,0]))
# s2 = list(set([7,8,9,0,2,3]))

# print(s1)
# print(s2)

# Sets do not maintain order
[0, 1, 2, 3, 4, 7, 8, 9]
[0, 2, 3, 7, 8, 9]


# maintain order with a dedupe function
s1 = [7,8,9,0,1,2,3,4,7,8,9,0]
s2 = [7,8,9,0,2,3]

def dedupe(lst):
    deduped_inorder = []
    for element in lst:
        if element not in deduped_inorder:
            deduped_inorder.append(element)
    return deduped_inorder

# print(dedupe(s1))
# print(dedupe(s2))

# maintained order
[7, 8, 9, 0, 1, 2, 3, 4]
[7, 8, 9, 0, 2, 3]



'''
Star (*) Args

'''
def star_args(*args):
    for item in args:
        print(item)
    return None

# star_args('hi', 56, int, [1,2,34,5,6])



'''
Union
'''

list1 = ['bear', 'cat', 'dog', 'dolphin', 'weasel']
list2 = ['bear', 'dog', 'elephant', 'weasel', 'mink', 'mountain lion']
list3 = ['bear', 'whale', 'sea cucumber', 'mink', 'eagle', 'dog']


def union(set1, set2):
    set_union = set1.copy()
    for item in set2:
        if item not in set_union:
            set_union.append(item)
    return set_union

# print(union(list1, list2))
['bear', 'cat', 'dog', 'dolphin', 'weasel', 'elephant', 'mink', 'mountain lion']


def union_mult_sets(*args):
    set_union = []

    for lst in args:
        for item in lst:
            if item not in set_union:
                set_union.append(item)
    return set_union

# print(union_mult_sets(list1, list2, list3))
['bear', 'cat', 'dog', 'dolphin', 'weasel', 'elephant', 'mink', 'mountain lion', 'whale', 'sea cucumber', 'eagle']



'''
Breakout Slide 8

'''

# Write out the sample space for the random experiment which is defined as sequentially completing the following steps:
# First, rolling a fair four-sided die
# Then, flipping a coin
# And finally, flipping the coin a second time
# 	{1HH, 1HT, 1TH ...

four_sided = [1,2,3,4]
fair_coin = ['H', 'T']

samp_space = []

for roll in four_sided:
    for flip1 in fair_coin:
        for flip2 in fair_coin:
            samp_space.append([roll, flip1, flip2])

# for outcome in samp_space:
#     print(outcome)


# List the sample points in the following events:
# A = The event in which the die roll results in exactly one pip showing
A = []
for outcome in samp_space:
    if outcome[0] == 1:
        A.append(outcome)

# print(A)
[[1, 'H', 'H'], [1, 'H', 'T'], [1, 'T', 'H'], [1, 'T', 'T']]


# B = The event in which at least one of the coin flips results in heads
B = []
for outcome in samp_space:
    if outcome.count('H') >= 1:
        B.append(outcome)
# print(B)
[[1, 'H', 'H'], [1, 'H', 'T'], [1, 'T', 'H'], [2, 'H', 'H'], [2, 'H', 'T'], [2, 'T', 'H'], [3, 'H', 'H'], [3, 'H', 'T'], [3, 'T', 'H'], [4, 'H', 'H'], [4, 'H', 'T'], [4, 'T', 'H']]

# List the sample points which are in the Union of events A and B from above
# print(union(A, B))
[[1, 'H', 'H'], [1, 'H', 'T'], [1, 'T', 'H'], [1, 'T', 'T'], [2, 'H', 'H'], [2, 'H', 'T'], [2, 'T', 'H'], [3, 'H', 'H'], [3, 'H', 'T'], [3, 'T', 'H'], [4, 'H', 'H'], [4, 'H', 'T'], [4, 'T', 'H']]




'''
Intersection
shared, not mutually exclusive elements
'''

list1 = ['bear', 'cat', 'dog', 'dolphin', 'weasel']
list2 = ['bear', 'dog', 'elephant', 'weasel', 'mink', 'mountain lion']
list3 = ['bear', 'whale', 'sea cucumber', 'mink', 'eagle', 'dog']


def intersection(set1, set2):
    set_intersect = []

    for item in set1:
        if item in set2:
            set_intersect.append(item)

    return set_intersect

# print(intersection(list1, list2))


def intersection_mult(*args):
    set_intersect = []

    if len(args) > 0:
        for item in args[0]:
            flag = True
            for set_ in args[1:]:
                if item not in set_:
                    flag = False
                    break
            if flag == True:
                set_intersect.append(item)
        return set_intersect
    else:
        return set_intersect

# print(intersection_mult())
[]  

# print(intersection_mult(list1, list2, list3))
['bear', 'dog']


'''
Set Difference
'''
list1 = ['bear', 'cat', 'dog', 'dolphin', 'weasel']
list2 = ['bear', 'dog', 'elephant', 'weasel', 'mink', 'mountain lion']
list3 = ['bear', 'whale', 'sea cucumber', 'mink', 'eagle', 'dog']


def difference(set1, set2):
    set_diff = []

    for item in set1:
        if item not in set2:
            set_diff.append(item)

    return set_diff


# print(difference(list1, list2))
['cat', 'dolphin']

# print(difference(list2, list1))
['elephant', 'mink', 'mountain lion']


'''
Complement
- requires the sample space to perform
'''
list1 = ['bear', 'cat', 'dog', 'dolphin', 'weasel']
list2 = ['bear', 'dog', 'elephant', 'weasel', 'mink', 'mountain lion']
list3 = ['bear', 'whale', 'sea cucumber', 'mink', 'eagle', 'dog']

sample_space = union_mult_sets(list1, list2, list3)


def complement(samp_space, set_):
    return difference(samp_space, set_)

# print(complement(sample_space, list3))
# ['cat', 'dolphin', 'weasel', 'elephant', 'mountain lion']


'''
Breakout Slide 13
'''

# Given the random experiment which is defined by four sequential flips of a fair coin, and the following events:
# A = There are 3 or more heads
# B = There are 2 or fewer tails
# C = All of the coins show the same face
# {HHHH, HHHT,
# List the sample points in each A, B, and C
coin_flips = ['H', 'T']

sample_space = []

for flip1 in coin_flips:
    for flip2 in coin_flips:
        for flip3 in coin_flips:
            for flip4 in coin_flips:
                sample_space.append([flip1, flip2, flip3, flip4, ])

# for samp in sample_space:
#     print(samp)

A, B, C = [], [], []

for outcome in sample_space:
    if outcome.count('H') >= 3:
        A.append(outcome)
    if outcome.count('T') <= 2:
        B.append(outcome)
    if outcome.count('H') == 4 or outcome.count('T') == 4:
        C.append(outcome)
    

# List the sample points in the set ACc
# "A intersect the complement of C"
# print(intersection(A, complement(sample_space, C)))
[['H', 'H', 'H', 'T'], ['H', 'H', 'T', 'H'], ['H', 'T', 'H', 'H'], ['T', 'H', 'H', 'H']]

# List the sample points in the set (AC)c
# print(complement(sample_space, intersection(A, C)))
[['H', 'H', 'H', 'T'], ['H', 'H', 'T', 'H'], ['H', 'H', 'T', 'T'], ['H', 'T', 'H', 'H'], ['H', 'T', 'H', 'T'], ['H', 'T', 'T', 'H'], ['H', 'T', 'T', 'T'], ['T', 'H', 'H', 'H'], ['T', 'H', 'H', 'T'], ['T', 'H', 'T', 'H'], ['T', 'H', 'T', 'T'], ['T', 'T', 'H', 'H'], ['T', 'T', 'H', 'T'], ['T', 'T', 'T', 'H'], ['T', 'T', 'T', 'T']]



'''
Breakout Slide 17
'''

# Let our sample space be rolling two 6-sided dice.
sample_space = []

for roll1 in range(1, 6+1):
    for roll2 in range(1, 6+1):
        sample_space.append([roll1, roll2])

# for outcome in sample_space:
#     print(outcome)

# Event A: any roll with a sum greater than or equal to 10
# Event B: any roll with an even sum

A, B = [], []

for outcome in sample_space:
    if sum(outcome) >= 10:
        A.append(outcome)
    if sum(outcome) % 2 == 0:
        B.append(outcome)

# What do our events A and B look like?
# print('A:')
# for outcome in A:
#     print(outcome)

# print()

# print('B:')
# for outcome in B:
#     print(outcome)

# What is A - B?
# print(difference(A, B))

# print()
# # What is B - A?
# print(difference(B, A))