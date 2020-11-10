'''
Factorial
'''
def factorial(num):
    prod = 1
    for n in range(2, (num+1)):
        prod *= n
    return prod

# print(factorial(5))


'''
Factorial Breakout Slide 10
There are ten people standing in a line for beignets at the world famous cafe du monde in New Orleans. How many different ways could the ten people be arranged in the queue?
10! = 3628800

Given that the line was formed organically (i.e, people got into line as they arrived without any organization or coordination), what is the probability that they are standing in the queue in alphabetical order. Assume everyone has a different last name?
 a b c d e f g h i j

 1 / 10!
'''
# print(factorial(10))


'''
Permutations
P(n, k) = n! / (n - k)!
'''

'''
You have 10 students and you are conducting a science fair where 4 students will win 1st, 2nd, 3rd, 4th. How many different arrangements of those 4 winners is possible?

g h i j
g h j i
g j h i
'''

def permutations(n, k):
    return int(factorial(n) / factorial(n-k))

# print(permutations(10, 4)) # 5040

print(permutations(10000, 5420))