setA = set(['bear', 'cat', 'dog', 'dolphin', 'weasel'])
setB = set(['bear', 'dog', 'elephant', 'weasel', 'mink', 'mountain lion'])
setC = set(['bear', 'whale', 'sea cucumber', 'mink', 'eagle', 'dog'])

sample_space = setA.union(setB).union(setC)


'''
Commutative
A U B = B U A
AB = BA
'''
# print(setA.union(setB) == setB.union(setA))
# print(setA.intersection(setB) == setB.intersection(setA))

a = True
b = False
c = True

print((a or b) == (b or a))
print((a and b) == (b and a))