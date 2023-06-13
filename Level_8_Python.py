library(reticulate)
########################################################################################################################################################################
# Codewars: Python Kata Level 8
########################################################################################################################################################################
# Multiple of index
# Return a new array consisting of elements which are multiple of their own index in input array (length > 1).

def multiple_of_index(arr):
    count = 0
    vec = list()
    for num in arr:
        if count == 0:
            if arr[count] == 0:
                vec.append(arr[count])
                count = count + 1
            else:
                count = count + 1
        elif arr[count] % count == 0:
            vec.append(arr[count])
            count = count + 1
        else:
            count = count + 1
    return vec
    pass
########################################################################################################################################################################
# Capitalization and Mutability
# Unfortunately, they have now left and the code they gave you doesn't work. Fix the helper function they wrote so that it works as intended (i.e. make the first character in the string "word" upper case).

def capitalize_word(word):
    return word.capitalize()





















































