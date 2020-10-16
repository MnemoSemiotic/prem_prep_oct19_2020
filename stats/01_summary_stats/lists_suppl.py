'''
lists are indexed collections of items
'''

animal_lst = ['dog', 'cat', 'bear']
#               0      1      2 

# print(animal_lst[0])
# print(animal_lst[1])
# print(animal_lst[2])

zero, one, two = animal_lst

# print(zero)
# print(one)
# print(two)

'''
range()
get us a series of numbers from x to z (not inclusive)
'''
x = 7
z = 25
# print(list(range(7, 25)))
# [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

'''
print out a list of the numbers from 24 to 364
'''
low = 24
high_incl = 364
high_excl = 365

# print(list(range(low, high_incl+1))) # communicates inclusion
# print(list(range(low, high_excl)))


'''
Generate a list of numbers from 10 to 20 (inclusive). Get the 6th item out of that list.
'''
# lst = list(range(10, 20+1))
# print(lst[5])


'''
Get a sublist from the first item to the 4th item in the range from 10 to 20 (inclusive)
'''
lst = list(range(10, 20+1))
sublist = (lst[0:3+1])
# print(sublist)

'''
Get a sublist from the 39th item to the 72nd item in a the range from 220 to 500 (inclusive)
'''

lst = list(range(220, 500+1))

# print(lst[38:72])


'''
Make a range of numbers from zero to 100 (exclusive)

'''
zero_to_100 = list(range(0,100))

# print(zero_to_100[0:len(zero_to_100):2])
# print(zero_to_100[0:len(zero_to_100):3])
# print(zero_to_100[0:len(zero_to_100):5])


'''
for loops

how we traverse a collection
'''

animal_lst = ['dog', 'cat', 'bear','octopus', 'squid', 'beaver', 'horse']

# for animal in animal_lst:
#     print(animal)


'''
Iterate through the range of numbers from zero to 100 (exclusive), and print all numbers that are divisible by both 2 and 3
'''
num_list = list(range(0, 100))

nums_div_2_and_3 = [] # accumulator/collector

for num in num_list:
    if num % 2 == 0 and num % 3 == 0:
        nums_div_2_and_3.append(num)

# print(nums_div_2_and_3)


'''
Iterate through the range of numbers from 0 to 1000 (exclusive), and collect into a new list called div_by_7_and_4 all numbers divisible by both 7 and 4
'''

num_list = list(range(0, 1000))

nums_div_7_and_4 = [] # accumulator/collector

for num in num_list:
    if num % 7 == 0 and num % 4 == 0:
        nums_div_7_and_4.append(num)

# print(nums_div_7_and_4)

'''
Write a function called get_div_by() that has 4 parameters: low, high, divisor_a, divisor_b

return a list of values from low to high (exclusive) that are divisible by both divisor_a and divisor_b
'''

def get_div_by(low, high, divisor_a, divisor_b):
    full_range = list(range(low, high))

    div_by = []

    for num in full_range:
        if num % divisor_a == 0 and num % divisor_b == 0:
            div_by.append(num)

    return div_by


# print(get_div_by(low=0, high=1000, divisor_a=7, divisor_b=4))
# print(get_div_by(low=0, high=10000, divisor_a=13, divisor_b=29))


'''
Extend the get_div_by() function to check divisibility for 3 numbers
'''

def get_div_by_3(low, high, divisor_a, divisor_b, divisor_c):
    full_range = list(range(low, high))

    div_by = []

    for num in full_range:
        if num % divisor_a == 0 and num % divisor_b == 0 and num % divisor_c == 0:
            div_by.append(num)

    return div_by

# print(get_div_by_3(low=0, high=1000, divisor_a=3, divisor_b=5, divisor_c=7))

# [0, 105, 210, 315, 420, 525, 630, 735, 840, 945]


'''
Extend the above function for an arbitrary number of divisors
'''
def get_div_by_nums(low, high, divisors):
    full_range = list(range(low, high))

    div_by = []

    for num in full_range:
        all_divisors = True
        for div in divisors:
            if num % div != 0:
                all_divisors = False
                break
        if all_divisors == True:
            div_by.append(num)

    return div_by

# print(get_div_by_nums(low=0, high=1000, divisors=[3,5,7]))
print(get_div_by_nums(low=0, high=10000, divisors=[3,5,7,11]))