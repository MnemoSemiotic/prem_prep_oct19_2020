def gen_4_bit_binary():
    bin_dct = dict()
    decimal = 0

    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    bin_dct[decimal] = [i,j,k,l]
                    decimal += 1
    return bin_dct

# for dec, bin_ in gen_4_bit_binary().items():
#     print(f'{dec}: {bin_}')


'''
7 minutes

Code the dec_to_bin function.
Should take as input 2 things:
    a decimal value (dec)
    a number of bits (n_bits=8)

algorithm
Given a decimal number
    - take the modulus by 2
        set aside the result
    - floor divide the number by 2
        until that number is 0
    - reverse the sequence of number that was set aside
'''

def dec_to_bin(dec, num_bits=8):
    bin_list = []
    x = dec

    for _ in range(num_bits):
        bit = x % 2
        bin_list.append(bit)
        x //= 2

    return bin_list[::-1] # list(reversed(bin_list))

# print(dec_to_bin(43))


def get_binary(n_bits=8):
    bins_d = dict()

    for dec in range(2**n_bits):
        bins_d[dec] = dec_to_bin(dec, n_bits)

    return bins_d


# for dec, bin_ in get_binary(n_bits=16).items():
#     print(f'{dec}: {bin_}')



'''
Construct binomial distr for n trials with prob=0.5 for each trial
'''

def binomial_distr(n_trials=8):
    binomial_dict = dict()

    bin_dict = get_binary(n_bits=n_trials)

    for _, binary in bin_dict.items():
        sum_bits = sum(binary)
        if sum_bits not in binomial_dict:
            binomial_dict[sum_bits] = 0
        binomial_dict[sum_bits] += 1

    return binomial_dict

d = binomial_distr(n_trials=8)

# for k, v in d.items():
#     print(f'{k}: {v}')

for k, v in d.items():
    print(f'{k}: {round(v / sum(d.values()), 4)}')