example_string = "the quick brown fox jumps over the lazy dog"

string_list = example_string.split()
giant_string = "".join(string_list)

print(giant_string)


mydict = {}

i=0
for letter in giant_string:
    if letter in mydict:
        mydict[letter] += 1
    else:
        mydict[letter]=1

#print(mydict)

sorted_letter_counts = sorted(mydict.items(), key=lambda x:x[1], reverse=True)

for pair in sorted_letter_counts:
    print(pair[0])

#print(mydict)
        
    