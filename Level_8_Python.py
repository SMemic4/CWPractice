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

def shortcut(s):
    les = list(s)
    s = ""
    vowels = ["a", "e", "i", "u"]
    for i in range(len(les)):
        if les[i] not in ["a", "e", "i", "o", "u"]:
            s += les[i]
        else:
            continue
    return s

########################################################################################################################################################################
# Super Duper Easy
# Make a function that returns the value multiplied by 50 and increased by 6. If the value entered is a string it should return "Error".

def problem(a):
    try:
        return a * 50 + 6
    except:
        return "Error"

########################################################################################################################################################################
# What is between?
# Complete the function that takes two integers (a, b, where a < b) and return an array of all integers between the input parameters, including them. For example:

def between(a,b):
    nums = list()
    while a <= b:
        nums.append(a)
        a += 1
    return nums

########################################################################################################################################################################
# Exclusive "or" (xor) Logical Operator
# Since we cannot define keywords in Javascript (well, at least I don't know how to do it), your task is to define a function xor(a, b) where a and b are the two expressions to be evaluated. Your xor function should have the behaviour described above, returning true if exactly one of the two expressions evaluate to true, false otherwise.

def xor(a,b):
    if a == True and b == True:
        return False
    elif a == False and b == False:
        return False
    else:
        return True
      
########################################################################################################################################################################      
# Plural
# e need a simple function that determines if a plural is needed or not. It should take a number, and return true if a plural should be used with that number or false if not. This would be useful when printing out a string such as 5 minutes,

def plural(n):
    if n == 1:
        return False
    else:
        return True
      
########################################################################################################################################################################      
# If/else syntax debug
# checkAlive/CheckAlive/check_alive should return true if the player's health is greater than 0 or false if it is 0 or below. The function receives one parameter health which will always be a whole number between -10 and 10.

def check_alive(health):
    return health > 0
  
########################################################################################################################################################################      
# What's the real floor?
# Write a function that given a floor in the american system returns the floor in the european system.
# With the 1st floor being replaced by the ground floor and the 13th floor being removed, the numbers move down to take their place. In case of above 13, they move down by two because there are two omitted numbers below them.

def get_real_floor(n):
    if n <= 0:
        return n
    elif n <= 13:
        return n-1
    elif n == 15:
        return 13
    else:
        return n - 2
      
########################################################################################################################################################################      
# Contamination #1 -String-
# This text is now fully mutated to this character.If the text or the character are empty, return an empty string. There will never be a case when both are empty as nothing is going on!!

def contamination(text, char):
    les = list(text)
    s = ""
    if len(les) == 0:
        return ""
    else:
        for i in range(len(les)):
            s += char
    return s

def contamination(text, char):
  return char * len(text)

########################################################################################################################################################################      
# Bin to Decimal
# Complete the function which converts a binary number (given as a string) to a decimal number.

def bin_to_decimal(inp):
    return int(inp, 2)

########################################################################################################################################################################      
# Find the position!
# When provided with a letter, return its position in the alphabet.

import string
def position(alphabet):
    letters = list(string.ascii_letters)
    return "Position of alphabet: " + str(letters.index(alphabet.lower()) + 1)

########################################################################################################################################################################      
# Add Length
# write a function that takes a String and returns an Array/list with the length of each word added to each element .
# "you will win" -->["you 3", "will 4", "win 3"]

def add_length(x):
    y = x.split(' ')
    for i in range(len(y)):
        y[i] += " " + str(len(y[i]))
    return y
  
########################################################################################################################################################################      
# Calculate BMI
# Write function bmi that calculates body mass index (bmi = weight / height2).

def bmi(weight, height):
    b = weight / height**2
    if b <= 18.5: return "Underweight"
    elif b <= 25.0: return "Normal"
    elif b <= 30.0: return "Overweight"
    else: return "Obese"

########################################################################################################################################################################      
# Debugging sayHello function
# The starship Enterprise has run into some problem when creating a program to greet everyone as they come aboard. It is your job to fix the code and get the program working again!
# Example Output: Hello, Mr. Spock

def say_hello(name):
    return "Hello, " + name

########################################################################################################################################################################      
# Find the smallest integer in the array
# Given an array of integers your solution should find the smallest integer.

def find_smallest_int(arr):
    return min(arr)

########################################################################################################################################################################      
# Multiply
# This code does not execute properly. Try to figure out why.

def multiply(a, b):
    return a * b

########################################################################################################################################################################    
# Convert boolean values to strings 'Yes' or 'No'
# Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.

def bool_to_word(boolean):
    if boolean: return "Yes"
    else: return "No"
    
########################################################################################################################################################################    
# Opposite number
# Very simple, given an integer or a floating-point number, find its opposite.

def opposite(number):
    return -number
  
########################################################################################################################################################################    
# Grasshopper - Summation
# Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.

def summation(num):
    return sum(list(range(1,num+1)))








































































