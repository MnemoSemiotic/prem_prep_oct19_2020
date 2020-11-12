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

# {4: 2, 5: 1}

def binary_sampling_dict(num_bits, num_samples=1000):
    d = dict()

    for _ in range(num_samples):
        binary = generate_n_bits(num_bits)
        k = sum(binary)

        if k not in d:
            d[k] = 0
        d[k] += 1

    return d

''' one trial of 1000 samples '''
d = binary_sampling_dict(num_bits=8, num_samples=1000)

# for k, v in sorted(d.items()):
#     print(f'{k}: {v}')


''' 500 trials of 1000 samples '''

def binary_sampling_clt(n_bits=8, num_samples=1000, num_sample_trials=500):
    d_out = dict()

    for _ in range(num_sample_trials):
        d = binary_sampling_dict(n_bits, num_samples)

        for k, v in d.items():
            if k not in d_out:
                d_out[k] = []
            d_out[k].append(v)

    for k, v in d_out.items():
        d_out[k] = sum(v) / len(v)
    
    return d_out

d = binary_sampling_clt(n_bits=8, num_samples=1000, num_sample_trials=500)

# for k, v in sorted(d.items()):
#     # print(f'{k}: {v}') # average counts
#     print(f'{k}: {v / sum(d.values())}') # averaged probability


''' ---------------- '''
''' using random, we can change our p val '''

def get_success(p=0.5):
    if random() < p:
        return 1
    else:
        return 0

def generate_n_successes(n=8, p=0.5):
    lst = []
    for _ in range(n):
        lst.append(get_success(p))

    return lst

# verify
# test_trials = 100000
# print([sum(generate_n_successes(12, p=0.25).count(1)) for _ in range(test_trials)]) / test_trials)


def binary_sampling_dict_vary_p(num_bits=8, p=0.5, num_samples=1000):
    d = dict()

    for _ in range(num_samples):
        binary = generate_n_successes(num_bits, p)
        k = sum(binary)

        if k not in d:
            d[k] = 0
        d[k] += 1

    return d

''' one trial of 1000 samples '''
d = binary_sampling_dict_vary_p(num_bits=8, p=0.3, num_samples=1000)

for k, v in sorted(d.items()):
    print(f'{k}: {v}')