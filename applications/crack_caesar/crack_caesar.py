# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

##read in the ciphertext
with open("ciphertext.txt") as f:
    words = f.read()

#print(words)
#words = words.strip('",\n.;)')


## get rid of punctuation
ignore_list = ' : ; , . - + = / \ | [ ] { } ( ) * ^ & ! ? \n  " - '


#

## make a dictionary that contains frequency of all the letters

letter_frequency = {}

for letter in words:
    if letter not in ignore_list:
        if letter in letter_frequency:
            letter_frequency[letter] += 1
        else:
            letter_frequency[letter] = 1
    #(letter)




## sort the dictionary by frequency of appearance



#print(letter_frequency)
sorted_frequency = sorted(letter_frequency.items(), key = lambda x: x[1], reverse=True)


cipher_letters_sorted = []

for pair in sorted_frequency:
    cipher_letters_sorted.append(pair[0])
    #print(pair[0], pair[1])

most_common_letters_sorted = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U','G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']


#print(cipher_letters_sorted)

#print(sorted_frequency)
## compare that sorted dictionary to a list of the known appearances
## make some sort of key to say, if this letter, then that letter

cipher_key = {}
i=0
for item in cipher_letters_sorted:
    # while i <= len(most_common_letters_sorted):
    if i >= len(most_common_letters_sorted):
        break
    cipher_key[item] = most_common_letters_sorted[i]
    i+=1

#print(cipher_key)
## go through each letter in the ciphertext and apply this key

#print(cipher_key['W'])

deciphered_string = ""
for letter in words:
    if letter in ignore_list:
        deciphered_string += letter
    elif letter in cipher_key:
        #print(cipher_key[letter])
        letter = cipher_key[letter]
        deciphered_string += letter
    else:
        letter = "•"

print(deciphered_string)