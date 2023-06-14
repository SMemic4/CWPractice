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

########################################################################################################################################################################    
# Reversed sequence
# Build a function that returns an array of integers from n to 1 where n>0. Example : n=5 --> [5,4,3,2,1]

def reverse_seq(n):
    x = range(1,n+1)
    les = list()
    for n in x:
        les.append(n)
    les.reverse()
    return les

########################################################################################################################################################################    
# Jenny's secret message
# Jenny has written a function that returns a greeting for a user. However, she's in love with Johnny, and would like to greet him slightly different. She added a special case to her function, but she made a mistake.

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else: 
        return "Hello, {name}!".format(name=name)
      
########################################################################################################################################################################          
# Array plus array
#  I want to get the sum of two arrays... Actually the sum of all their elements.

def array_plus_array(arr1,arr2):
        return sum(arr1 + arr2)

########################################################################################################################################################################          
# Pillars
# There are pillars near the road. The distance between the pillars is the same and the width of the pillars is the same. Your function accepts three arguments:
# number of pillars (≥ 1); distance between pillars (10 - 30 meters); width of the pillar (10 - 50 centimeters).
# Calculate the distance between the first and the last pillar in centimeters (without the width of the first and last pillar).

def pillars(num_pill, dist, width):
    return (num_pill - 1) * dist * 100 + width * max(0, num_pill - 2)

########################################################################################################################################################################          
# Be Concise IV - Index of an element in an array
# Provided is a function Kata which accepts two parameters in the following order: array, element and returns the index of the element if found and "Not found" otherwise. Your task is to shorten the code as much as possible in order to meet the strict character count requirements of the Kata. (no more than 161) You may assume that all array elements are unique.

def find(a, e):
    try:return a.index(e)
    except:return "Not found"
    
########################################################################################################################################################################          
# Calculate average
# Write a function which calculates the average of the numbers in a given list.

def find_average(numbers):
    try: return sum(numbers)/len(numbers)
    except: return 0

def find_average(array):
    return sum(array) / len(array) if array else 0

########################################################################################################################################################################          
# Beginner Series #1 School Paperwork
# Your classmates asked you to copy some paperwork for them. You know that there are 'n' classmates and the paperwork has 'm' pages.
# Your task is to calculate how many blank pages do you need. If n < 0 or m < 0 return 0.

def paperwork(n, m):
    if n > 0 and m > 0: return n * m
    else: return 0

########################################################################################################################################################################          
# Total amount of points
# write a function that takes this collection and returns the number of points our team (x) got in the championship by the rules given above.

def points(games):
    total = 0
    for i in games:
        x = i[0]
        y = i[2]
        if x > y:
            total += 3
        elif x == y:
            total += 1
        else:
            total += 0
    return total
  
########################################################################################################################################################################          
# Keep Hydrated
# Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling. You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest value.
  
import math
def litres(time):
    return(math.floor(time/2))
  
########################################################################################################################################################################          
# Count the number of cubes with paint on

def count_squares(cuts):
    if cuts == 0: return 0
    return (6 * cuts * cuts) + 2

########################################################################################################################################################################          
# Thinkful - Logic Drills: Traffic light
# ou need a function to handle each change from green, to yellow, to red, and then to green again.

def update_light(current):
    if current == "green":
        return "yellow"
    elif current == "yellow":
        return "red"
    else:
        return "green"

########################################################################################################################################################################          
# Is he gonna survive?
# Assuming he's gonna grab a specific given number of bullets and move forward to fight another specific given number of dragons, will he survive?

def hero(bullets, dragons):
    return bullets >= dragons * 2

########################################################################################################################################################################          
# Quadrants
# Given a point in a Euclidean plane (x and y), return the quadrant the point exists in: 1, 2, 3 or 4 (integer). x and y are non-zero integers, therefore the given point never lies on the axes.

def quadrant(x, y):
    if x > 0:
        if y > 0:
            return 1
        else: return 4
    else: 
        if y > 0: return 2
        else: return 3

########################################################################################################################################################################          
# Find the Integral
# In order to find the integral all you need to do is add one to the exponent (the second argument), and divide the coefficient (the first argument) by that new number.
# For example for 3x^2, the integral would be 1x^3: we added 1 to the exponent, and divided the coefficient by that new number).

def integrate(coefficient, exponent):
    x = int(coefficient / (exponent +1))
    y = exponent + 1
    return str(x) +"x^" + str(y)

########################################################################################################################################################################            
# Take the Derivative
# Write a function that finds the derivative

def derive(coefficient, exponent): 
    x = int(coefficient * exponent)
    y = exponent - 1
    return str(x) +"x^" + str(y)

########################################################################################################################################################################            
# 5 without numbers !!
# Sounds easy right? Just bear in mind that you can't use any of the following characters: 0123456789*+-/

def unusual_five():
    return sum([True, True, True, True, True])
  
########################################################################################################################################################################            
# Return Negative
# In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?

def make_negative( number ):
    if number == 0: return 0
    elif number > 0: return number * -1
    else: return numbe
    
########################################################################################################################################################################            
# Expressions Matter
# Given three integers a ,b ,c, return the largest number obtained after inserting the following operators and brackets: +, *, ()
    
def expression_matter(a, b, c):
    return max([(a * (b +c)), (a*b*c), (a + b * c), ((a +b) * c), (a + b + c)])   
    
########################################################################################################################################################################              
# DNA to RNA Conversion    
# Create a function which translates a given DNA string into RNA. "GCAT"  =>  "GCAU"
  
  
def dna_to_rna(dna):
    dna = list(dna)
    ex = ""
    n = 0
    for i in dna:
        if dna[n] == "T":
            dna[n] = "U"
            n = n + 1
        else:
            n = n + 1
    for i in dna:
        ex += i
    return ex    
########################################################################################################################################################################











































































