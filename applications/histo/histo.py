# Your code here


#This function takes a single filename string as an argument
def histogram(filename_string):
    #It should open the file, and work through it to produce the output.
    with open(filename_string) as f:
        words = f.read()


#     Print a histogram showing the word count for each word, one hash mark
# for every occurrence of the word.

    #create a dict to keep track of this
    word_count = {}



    ## Split string
    split_words = words.split()
    #  iterate through each word
    for word in split_words:
        #Case should be ignored, and all output forced to lowercase.
        word = word.lower()
        #Ignore each of the following characters:
        word = word.strip('" : ; , . - + = / \ | [ ] { } ( ) * ^ &')
        #If the input contains no ignored characters, print nothing.
        if word == "":
            return ""

        if word in word_count:
            word_count[word] += '#'
        else:
            word_count[word] = '#'

    #print(split_words)
   
    #sorted(word_count)
    # print(word_count)

    # sorted_word_counts = sorted(word_count.items()

    #sorting it by first the number of ##, then the alphabetical order

    sorted_word_counts = sorted(word_count.items(), key=lambda x:x[1] + x[0], reverse=False)

    #print(sorted_word_counts)

    # Print a histogram showing the word count for each word, one hash mark
    # for every occurrence of the word.

    #     Output will be first ordered by the number of words, then by the word
    # (alphabetically).

    #     The hash marks should be left justified two spaces after the longest
    # word.
    max_len = 0
    for item in sorted_word_counts:
        
        # if len(item)
        #print(len(item[0]))
        if len(item[0]) > max_len:
            max_len = len(item[0])
    print(max_len)
    # max_len is 15

    for pair in sorted_word_counts:
        #print(len(pair[0]))
        print(pair[0] + ((max_len - len(pair[0])+2) * " ") + pair[1])



# call the function
histogram('robin.txt')