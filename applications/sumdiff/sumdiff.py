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
# a = q[int(random.random()*len(q))]
# b = q[int(random.random()*len(q))]
# c = q[int(random.random()*len(q))]
# d = q[int(random.random()*len(q))]

# print(a,b,c,d)
# #What are the combinations of f(a) + f(b) that are algebraically equivalent to the combinations of f(c) - f(d)?

# a_and_b = f(a) + f(b)
# print(a_and_b)

# c_and_d = f(c) - f(d)
# print(c_and_d)

result_dict = {}

for item in q:
    for second_item in q:
        left_result = f(item)+f(second_item)
        #print(f'f({item}) + f({second_item}) = {left_result}')

        # save these results in a dictionary

        

        result_dict[(item, second_item)] = left_result

for item in q:
    for second_item in q:
        right_result = f(item)-f(second_item)
        #print(right_result)
        #print(f'f({item}) + f({second_item}) = {right_result}')
        if right_result in result_dict.values():
            # result_dict[]
            print("FOUND")

            for key, value in result_dict.items():
                if right_result == value:
                    print(f'left side f({key[0]}) + f({key[1]}) = {value}')
        
                    #print(key)
            #print(f'left side f({result_dict}) - f({second_item}) = {right_result}')
            print(f'right side f({item}) - f({second_item}) = {right_result}')

        # result_dict[(item, second_item)] = left_result

#print(result_dict.values())


# compare the left and right dictionaries
# return the place where they overlap

#result_dict[result_dict.values == 20]

        

def get_key(val): 
    for key, value in my_dict.items(): 
         if val == value: 
             return key 
    #print(item)

