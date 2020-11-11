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