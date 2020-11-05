'''
Random Experiment
'''

from random import choice

def coin_flip():
    return choice(['H', 'T'])

# print(coin_flip())

# 20 flips
def twenty_flips():
    twenty_flips_ = []

    for _ in range(20):
        twenty_flips_.append(coin_flip())

    return twenty_flips_.count('H')

'''
How many Heads would you "Expect" in 20 flips?
0.5 * 20 = 10
'''

# result_of_heads_20_flips = []

# for _ in range(100000):
#     result_of_heads_20_flips.append(twenty_flips())

# print(sum(result_of_heads_20_flips) / 100000)


'''
list/set trick
- removing duplicates through the essence of a set
'''

# lst = [8,4,6,4,5,3,4,6,8,4,6,3,5,4,6,8,4,7]
# l1 = list(set(lst))
# print(l1) # [3, 4, 5, 6, 7, 8]


def dedupe_in_order(lst):
    deduped = []
    for element in lst:
        if element not in deduped:
            deduped.append(element)
    return deduped

# print(dedupe_in_order(lst))


'''
Star (*) Args
'''
def star_args(*args):
    for item in args:
        print(item)
    return None

# star_args('hi', 43, True, [1,2,3,4,5,6], 3.2)



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


def union_mult_sets(*args):
    set_union = []

    # print(type(args)) # Surprise! *args is a tuple!

    for lst in args:
        for item in lst:
            if item not in set_union:
                set_union.append(item)
        
    return set_union

# print(union_mult_sets(list1, list2, list3))


'''
Intersection

'''
def intersection(set1, set2):
    set_intersect = []

    for item in set1:
        if item in set2:
            set_intersect.append(item)
    return set_intersect

# print(intersection(list1, list2))

def intersection_mult(*args):
    set_intersect = []

    if len(args) > 0 and len(args[0]) > 0:
        for item in args[0]:
            is_member = True
            for set_ in args[1:]:
                if item not in set_:
                    is_member = False
                    break
            if is_member:
                set_intersect.append(item)

        return set_intersect
    else:
        return set_intersect

# print(intersection_mult(list1, list2, list3))



'''
Set Difference
'''

def difference(set1, set2):
    set_diff = []

    for item in set1:
        if item not in set2:
            set_diff.append(item)
    
    return set_diff

# print(difference(list1, list2))

# print(difference(list2, list1))



'''
Complement
- requires the sample space
'''

list1 = ['bear', 'cat', 'dog', 'dolphin', 'weasel'] 
list2 = ['bear', 'dog', 'elephant', 'weasel', 'mink', 'mountain lion']
list3 = ['bear', 'whale', 'sea cucumber', 'mink', 'eagle', 'dog']

extra_stuff = ['badger', 'hawk']

sample_space = union_mult_sets(list1, list2, list3, extra_stuff)
# print(sample_space)

def complement(samp_space, set1):
    return difference(samp_space, set1)

# print(complement(sample_space, union(list1, list2)))


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

for outcome in samp_space:
    print(outcome)