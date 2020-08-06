import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here


#split into words
words = words.split()

#print(words)

#build up dataset of which words follow other words
#use a hash table

words_dataset = {}

#iterate through the list of split words

for i in range(len(words)-1):
    word = words[i]
    next_word = words[i+1]

    if word not in words_dataset:
        words_dataset[word] = [next_word]

    else:
        words_dataset[word].append(next_word)

#print(words_dataset)


#choose random start word to begin

#start words
start_words = [] # quotes or capital

for key in words_dataset.keys():
    if key[0].isupper() or len(key) > 1 and key[1].isupper():
        start_words.append(key)

#print(start_words)

#chooses random word out of list
#random.choice()

random_start_word = random.choice(start_words)
#print(random_start_word)

random_next_word = random.choice(words_dataset[random_start_word])


#stop words
stop_words = [".?!"] #or puncutaion followed by ""
# first or secds char is capitalized

## make a loop that:
#prints the word
## stop on stop word
# else randomly choose a word to follow this one

stopped = False
while not stopped:
    if random_next_word[-1] in stop_words or len(random_next_word) > 1 and random_next_word[-2] in stop_words:
        stopped = True
    print(random_start_word)
    print(random_next_word)


### THIS just needs  a little more workt o make the while loop not run inifnitely




# TODO: construct 5 random sentences
# Your code here



