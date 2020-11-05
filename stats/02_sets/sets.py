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

lst = [8,4,6,4,5,3,4,6,8,4,6,3,5,4,6,8,4,7]
l1 = list(set(lst))
print(l1) # [3, 4, 5, 6, 7, 8]


def dedupe_in_order(lst):
    deduped = []
    for element in lst:
        if element not in deduped:
            deduped.append(element)
    return deduped

print(dedupe_in_order(lst))