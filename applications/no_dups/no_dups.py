def no_dups(s):
    # Your code here

    # same order
    # duplicates removed
    #use a cache
    duplicate_checker = {}

    split_string = s.split()

    no_dups = []

    #print(split_string)
    
     # go through each word in the string
    # if it hasn't been seen before, add to the dup checker AND append to a new list
    # if it HAS been seen before, add to dup checker and don't append

    if split_string == "":
        return ""
    for word in split_string:
        if word in duplicate_checker:
            duplicate_checker[word] += 1
        else:
            duplicate_checker[word] = 1
            no_dups.append(word)

    #print(duplicate_checker)

    # now print in the same order but check to see if word is a duplicate
    
    # no_dups = no_dups.join("")
    # giant_string = "".join(string_list)


    no_dups = " ".join(no_dups)
   

    
    # for word in split_string:
    #     if duplicate_checker[word] == 1:
    #         no_dups.append(word)

    #print(no_dups)
    return no_dups



    # no extra spaces



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))