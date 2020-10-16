from random import choice, random

'''
using choice we are limited to a fixed value of p
'''

def get_bit():
    return choice([0, 1])

def generate_n_bits(n=8):
    lst = []
    for _ in range(n):
        lst.append(get_bit())

    return lst

# print(generate_n_bits(12))

'''
Write a function called binary_sampling_dict that has two parameters
    num_bits
    num_samples

return a dictionary where the keys represent the number of successes, and the values associated with those keys represent the count of that number of successes occurring
'''
def binary_sampling_dict(num_bits=8, num_samples=1000):
    d = dict()

    for _ in range(num_samples):
        binary = generate_n_bits(num_bits)
        sum_bits = sum(binary)

        if sum_bits not in d:
            d[sum_bits] = 0
        d[sum_bits] += 1

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

# d = binary_sampling_clt(n_bits=8, num_samples=1000, num_sample_trials=500)

# for k, v in sorted(d.items()):
#     # print(f'{k}: {v}') # for counts
#     print(f'{k}: {v / sum(d.values())}') # for counts
            

''' ---------------------------------- '''
''' using random, we can change our p value '''


def get_trial_result(p=0.5):
    if random() < p:
        return 1
    else:
        return 0

def generate_n_trials(n=8, p=0.5):
    lst = []
    for _ in range(n):
        lst.append(get_trial_result(p))

    return lst

# # verify this is working
# test_trials = 100000
# print(sum([generate_n_trials(12, p=0.25).count(1) for _ in range(test_trials)]) / test_trials)

'''
Write a function called binary_sampling_dict that has two parameters
    num_bits
    num_samples

return a dictionary where the keys represent the number of successes, and the values associated with those keys represent the count of that number of successes occurring
'''
def binary_sampling_dict_vary_p(num_bits=8, p=0.5, num_samples=1000):
    d = dict()

    for _ in range(num_samples):
        binary = generate_n_trials(num_bits, p)
        sum_bits = sum(binary)

        if sum_bits not in d:
            d[sum_bits] = 0
        d[sum_bits] += 1

    return d

''' one trial of 1000 samples '''
# d = binary_sampling_dict_vary_p(num_bits=12, p=0.25, num_samples=1000)

# for k, v in sorted(d.items()):
#     print(f'{k}: {v}')


''' 500 trials of 1000 samples '''
def binary_sampling_clt_vary_p(n_bits=8, p=0.5, num_samples=1000, num_sample_trials=500):
    d_out = dict()

    for _ in range(num_sample_trials):
        d = binary_sampling_dict_vary_p(n_bits, p, num_samples)

        for k, v in d.items():
            if k not in d_out:
                d_out[k] = []
            d_out[k].append(v)

    for k, v in d_out.items():
        d_out[k] = sum(v) / len(v)

    return d_out

d = binary_sampling_clt_vary_p(n_bits=12, p=0.25, num_samples=1000, num_sample_trials=500)

for k, v in sorted(d.items()):
    # print(f'{k}: {v}') # for counts
    print(f'{k}: {v / sum(d.values())}') # for counts
            


