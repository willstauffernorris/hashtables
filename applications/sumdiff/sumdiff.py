import random
"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here

#If you choose 4 numbers from q, call them a, b, c, and d:
#random_int = int(random.random()*len(q))
a = q[int(random.random()*len(q))]
b = q[int(random.random()*len(q))]
c = q[int(random.random()*len(q))]
d = q[int(random.random()*len(q))]

print(a,b,c,d)
#What are the combinations of f(a) + f(b) that are algebraically equivalent to the combinations of f(c) - f(d)?