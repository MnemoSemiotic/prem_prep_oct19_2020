from random import choice, random

'''
using choice we are limited to a fixed p value
'''

def get_bit():
    return choice([0,1])

def generate_n_bits(n=8):
    lst = []
    for _ in range(n):
        lst.append(get_bit())

    return lst

# print(generate_n_bits(n=16))

'''
Write a function called binary_sampling_dict that has two params
    num_bits
    num_samples

return a dict where the keys repr the number of successes,
and the values associated with those keys represent the count
of that number of successes occurring.
'''
# 001011010 : 4 successes
# 101011000 : 4 successes
# 101011010 : 5 successes

# {4: 2}

def binary_sampling_dict(num_bits, num_samples=1000):
