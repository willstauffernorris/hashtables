def word_count(s):
    # Your code here

    if s == "":
        return {}

    # return a dict of words and their counts

    # split string
    split_string = s.split()

    #split_string = split_string.str.lower()

    # create dict
    counter = {}
    ignore_list = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'

    #print(split_string)

    
    # print(split_string)
    for word in split_string:
        word = word.lower()
        # print(word)
        word = word.strip('" : ; , . - + = / \ | [ ] { } ( ) * ^ &')
        # for letter in word:
        #     if letter in ignore_list:
        #         #print(word[0])
        #         print(letter)
        #         #word[letter] = word[word.index(letter)].remove(letter)
        #         #print(letter)
        #         #print(word.index(letter))
        #         print(word[word.index(letter)])
        #         word[word.index(letter)] = ""
        #         #print(word[word.index(letter)])
        #         # print(word[word.index(letter)])
        #         # word.pop(word.index(letter))
        #     #print(letter)
        
        # print(word)
        if word == "":
            return counter


        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1
    #print(s)
    #print(counter)
    return counter




if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))