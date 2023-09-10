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
# Function 1- Hello World
# Make a simple function called greet that returns the most-famous "hello world!".

def greet():
    return "hello world!"
  
########################################################################################################################################################################              
# Is n divisible by x and y?
# Create a function that checks if a number n is divisible by two numbers x AND y. All inputs are positive, non-zero numbers.

def is_divisible(n,x,y):
    if n % x == 0 and n % y == 0:
        return True
    else:
        return False

########################################################################################################################################################################              
# Did she say hallo?
# Write a simple function to check if the string contains the word hallo in different languages.

def validate_hello(greetings):
    les = ["hello", "ciao", "salut", "hallo", "hola", "ahoj","czesc"]
    for i in les:
            if greetings.lower().find(i) != -1:
                return True
    return False
  
def validate_hello(greetings):
    return any(x in greetings.lower() for x in ['hello','ciao','salut','hallo','hola','ahoj','czesc'])

########################################################################################################################################################################              
# Name Shuffler
# Write a function that returns a string in which firstname is swapped with last name.

def name_shuffler(str):
    str = str.split(" ")
    str.reverse()
    x = ""
    for i in str:
        x += i 
        x += " "
    return x.rstrip()

def name_shuffler(str_):
    [first, last] = str_.split()
    return last + " " + first

########################################################################################################################################################################              
# Find Multiples of a Number
# build a program that takes a value, integer , and returns a list of its multiples up to another value, limit . If limit is a multiple of integer, it should be included as well. There will only ever be positive integers passed into the function, not consisting of 0. The limit will always be higher than the base.

def find_multiples(integer, limit):
    les = list()
    x = integer
    while integer <= limit:
        les.append(integer)
        integer += x
    return les

def find_multiples(integer, limit):
    return list(range(integer, limit+1, integer))
  
  
########################################################################################################################################################################              
# Grasshopper- Check for factor
# This function should test if the factor is a factor of base. Return true if it is a factor or false if it is not.

def check_for_factor(base, factor):
    return base % factor == 0


########################################################################################################################################################################              
# Convert number to reversed array of digits
# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

def digitize(n):
    n = str(n)
    les = list(n)
    les.reverse()
    sel = list()
    for i in les:
        sel.append(int(i))
    return sel

########################################################################################################################################################################              
########################################################################################################################################################################     
# Convert a string to an array
# Write a function to split a string and convert it into an array of words.

def string_to_array(s):
    les1 = [""]
    if s is "":
        return les1
    s = s.split()
    s = list(s)
    return s

########################################################################################################################################################################     
# MakeUpperCase
# Write a function which converts the input string to uppercase.

def make_upper_case(s):
    return s.upper()

########################################################################################################################################################################     
# A Needle in the Haystack
# Write a function findNeedle() that takes an array full of junk but containing one "needle"

def find_needle(haystack):
    return "found the needle at position " + str(haystack.index("needle"))

########################################################################################################################################################################     
# Sentence Smash
# Write a function that takes an array of words and smashes them together into a sentence and returns the sentence. You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word. Be careful, there shouldn't be a space at the beginning or the end of the sentence!

def smash(words):
    x = ""
    for word in words:
        x += " " + word
    return x[1:]
  
########################################################################################################################################################################     
# L1: Set Alarm
# The function should return true if you are employed and not on vacation (because these are the circumstances under which you need to set an alarm). It should return false otherwise. Examples:

def set_alarm(employed, vacation):
    if employed is True and vacation is False:
        return True
    else:
        return False
      
########################################################################################################################################################################     
# Price of Mangoes
# There's a "3 for 2" (or "2+1" if you like) offer on mangoes. For a given quantity and price (per mango), calculate the total cost of the mangoes.

def mango(quantity, price):
    return ((quantity - int(quantity/3))  * price)

########################################################################################################################################################################     
# Short Long Short
# Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. The strings will not be the same length, but they may be empty ( zero length ).

def solution(a, b):
    if len(a) < len(b):
        return a + b + a
    else:
        return b + a + b
      
########################################################################################################################################################################       
# Student's Final Grade
# Create a function finalGrade, which calculates the final grade of a student depending on two parameters: a grade for the exam and a number of completed projects.

def final_grade(exam, projects):
    if exam > 90 or projects > 10:
        return 100
    elif exam > 75 and projects >= 5:
        return 90
    elif exam > 50 and projects >= 2: 
        return 75
    else:
        return 0 

########################################################################################################################################################################       
# Convert a Boolean to a String
# Implement a function which convert the given boolean value into its string representation.

def boolean_to_string(b):
    return str(b)
  
########################################################################################################################################################################       
# Counting sheep...
# Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).

def count_sheeps(sheep):
    count = 0
    for x in sheep:
        if x == True:
            count += 1
    return count

########################################################################################################################################################################            
# Returning Strings
# Make a function that will return a greeting statement that uses an input; your program should return, "Hello, <name> how are you doing today?".

def greet(name):
    return "Hello, " + name + " how are you doing today?"
  
########################################################################################################################################################################            
# Sun of positives
# You get an array of numbers, return the sum of all of the positives ones.
  
def positive_sum(arr):
    count = 0
    for x in arr:
        if x > 0:
            count += x
    return count 

########################################################################################################################################################################            
# Is it a palindrome?
# Write a function that checks if a given string (case insensitive) is a palindrome. A palindrome is a word, number, phrase, or other sequence of symbols that reads the same backwards as forwards, such as madam or racecar, the date and time 12/21/33 12:21, and the sentence: "A man, a plan, a canal – Panama".

def is_palindrome(s):
    return s.lower() == s[::-1].lower()

  
########################################################################################################################################################################            
# Opposites Attract
# Write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't.
  
def lovefunc( flower1, flower2 ):
    return (flower1 + flower2) % 2 != 0  
  
########################################################################################################################################################################            
# Get the mean of an array
# Return the average of the given array rounded down to its nearest integer.
  
def get_average(marks):
    return int(sum(marks)/len(marks))
  
########################################################################################################################################################################              
# Abbreviate a Two Word Name
# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
  
def abbrev_name(name):
    return name[0].upper() + "." + name[name.find(" ") + 1].upper()  
  
########################################################################################################################################################################              
# Is the string uppercase?
# Create a method to see whether the string is ALL CAPS.
  
def is_uppercase(inp):
    return inp == inp.upper()  
  
########################################################################################################################################################################              
# Quadratic Coefficients Solver
# find the coefficients of quadratic equation of the given two roots

def quadratic(x1, x2):
    return( 1, -(x1 + x2), x1 * x2)  
  
########################################################################################################################################################################              
# Count Odd Numbers below n
# Given a number n, return the number of positive odd numbers below n, EASY!

def odd_count(n):
    return int(n / 2)

########################################################################################################################################################################              
# String Repeat
# Write a function that accepts an integer n and a string s as parameters, and returns a string of s repeated exactly n times.

def repeat_str(repeat, string):
    return string * repeat

########################################################################################################################################################################              
# Century From Year
# Given a year, return the century it is in.

def century(year):
    return (year + 99) // 100

########################################################################################################################################################################              
# Reversed Strings
# Complete the solution so that it reverses the string passed into it.

def solution(string):
    return string[::-1]

########################################################################################################################################################################              
# Reversed Words
# Complete the solution so that it reverses all of the words within the string passed in.

def reverse_words(s):
    les = list(s.split())
    les.reverse()
    return " ".join(les)
  
  
########################################################################################################################################################################              
# Beginner Series #2 Clock
# Clock shows h hours, m minutes and s seconds after midnight. Your task is to write a function which returns the time since midnight in milliseconds.
  
def past(h, m, s):
    return h * 3600000 + m * 60000 + s * 1000;  
  
########################################################################################################################################################################              
# POwers of 2
# Complete the function that takes a non-negative integer n as input, and returns a list of all the powers of 2 with the exponent ranging from 0 to n ( inclusive ).
  
def powers_of_two(n):
    les = range(0, n+1)
    a = list()
    for x in les:
        a.append(2**x)
    return a  
  
########################################################################################################################################################################              
# Simple multiplication
# This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.

def simple_multiplication(number) :
    if number % 2 == 0: return number * 8
    else: return number * 9

########################################################################################################################################################################              
# Find Nearest square number
# Your task is to find the nearest square number, nearest_sq(n) or nearestSq(n), of a positive integer n.

import math
def nearest_sq(n):
    return round(math.sqrt(n)) ** 2
  
########################################################################################################################################################################              
# Remove String Spaces
# Write a function that removes the spaces from the string, then return the resultant string.

def no_space(x):
    return x.replace(" ", "")

########################################################################################################################################################################              
# Remove String Spaces
# Write a function that removes the spaces from the string, then return the resultant string.

def no_space(x):
    return x.replace(' ' ,'')
########################################################################################################################################################################              
# True or False? (Beginner)
# Write a function that returns false without using False
  
def if_chuck_says_so():
    return 0 == 1
  
########################################################################################################################################################################       
# Power
# The goal is to create a function of two inputs number and power, that "raises" the number up to power (ie multiplies number by itself power times).

def number_to_pwr(number, p): 
    if p == 0:
        return 1
    else:
        count = 1
        number1 = number
        while (count <= p -1):
            number1 = number1 * number
            count += 1
    return number1
  
########################################################################################################################################################################       
# All Star Code Challenge #18
# Create a function that accepts a string and a single character, and returns an integer of the count of occurrences the 2nd argument is found in the first one.

def str_count(strng, letter):
    count = 0
    les = list(strng)
    for x in les:
        if x == letter:
            count += 1
    return count

return string.count(letter)

########################################################################################################################################################################       
# Square(n) Sum
# Complete the square sum function so that it squares each number passed into it and then sums the results together.

def square_sum(numbers):
    total = 0
    for x in numbers:
        total = total + x ** 2
    return total

def square_sum(numbers):
    return sum(x ** 2 for x in numbers)

########################################################################################################################################################################       
# Even or Odd
# Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

########################################################################################################################################################################       
# Return to Sanity
# This function should return an object, but it's not doing what's intended. What's wrong?

def mystery():
    results = {
    'sanity': 'Hello'}
    return results

########################################################################################################################################################################       
# Lario and Muigi Pipe Problem
# Given the a list of numbers, return a fixed list so that the values increment by 1 for each index from the minimum value up to the maximum value (both included).

def pipe_fix(nums):
    return list(range(min(nums), max(nums)+1))

########################################################################################################################################################################       
# Twice as old
# Сalculate how many years ago the father was twice as old as his son (or in how many years he will be twice as old). The answer is always greater or equal to 0, no matter if it was in the past or it is in the future.

def twice_as_old(dad_years_old, son_years_old):
    return abs(son_years_old * 2 - dad_years_old)

########################################################################################################################################################################       
# Beginner - Reduce but Grow
# Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

def grow(arr):
    total = 1
    for x in arr:
        total = total * x
    return total 
  
########################################################################################################################################################################       
# Volume of a Cuboid
# Write a function to calculate the volume of a cuboid with three values: the length, width and height of the cuboid

def get_volume_of_cuboid(length, width, height):
    return length * width * height
  
########################################################################################################################################################################       
# You Can't Code Under Pressure #1
# Code as fast as you can! You need to double the integer and return it.

def double_integer(i):
    return i * 2

########################################################################################################################################################################       
# Get Nth Even Number
# Return the Nth Even Number

def nth_even(n):
    return n * 2 - 2

########################################################################################################################################################################       
# Invert values
# Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

def invert(lst):
    les = list()
    for x in lst:
        les.append(-x)
    return les

def invert(lst):
    return [-x for x in lst]

########################################################################################################################################################################       
# Function 2 - squaring an argument
# Now you have to write a function that takes an argument and returns the square of it.

def square(n):
    return n ** 2

########################################################################################################################################################################       
# Removing Elements
# Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.

def remove_every_other(my_list):
    if len(my_list) == 1:
        return my_list
    else:
        les = list()
        count = 0
        while count < len(my_list):
            les.append(my_list[count])
            count += 2
        return les

def remove_every_other(my_list):
    return my_list[::2]

########################################################################################################################################################################       
# Remove the time
# Write a function that takes the website date/time in its original string format and returns the shortened format.

def shorten_to_date(long_date):
    return long_date[0:long_date.find(",")]

########################################################################################################################################################################       
# Vexing Vanishing Values
# accept a list of values, and another value n, then return a new list with every value multiplied by n. For example, [1, 2, 3] and 4 should result in [4, 8, 12].

def mul_by_n(lst, n):
    return [x * n for x in lst]

########################################################################################################################################################################       
# Kata Example Twist
# Add the value "codewars" to the array websites 1,000 times.

websites = []
count = 0
while count < 1000:
    websites.append("codewars")
    count += 1

websites = ["codewars"] * 1000

########################################################################################################################################################################       
# Grasshopper - Messi goals function
# Complete the function to return his total number of goals in all three leagues.

def goals(laLiga, copaDelRey, championsLeague):
    return laLiga + copaDelRey + championsLeague
  
########################################################################################################################################################################       
# BASIC: Making Six Toast.
# Define a function that counts how many more (or less) pieces of toast you need in the toasters. Even though you need more or less, the number will still be positive, not negative.
  
  def six_toast(num):
    if num < 6:
        return 6 - num
    else:
        return num - 6 
  
########################################################################################################################################################################   
# Third Angle of a Triangle
# You are given two interior angles (in degrees) of a triangle. Write a function to return the 3rd.
  
def other_angle(a, b):
    return 180 - a - b  
  
########################################################################################################################################################################   
# The Feast of Many Beasts
# Write a function feast that takes the animal's name and dish as arguments and returns true or false to indicate whether the beast is allowed to bring the dish to the feast.
# here is just one rule: the dish must start and end with the same letters as the animal's name

def feast(beast, dish):
    return beast[0] == dish[0] and beast[-1] == dish[-1]

########################################################################################################################################################################   
# If you can't sleep, just count sheep!!
# Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers.

def count_sheep(n):
    if n == 0:
        return ""
    else:
        count = 1
        x = ""
        while count <= n:
            x += str(count) + " sheep..."
            count += 1
    return x

def count_sheep(n):
    return ''.join(f"{i} sheep..." for i in range(1,n+1))


########################################################################################################################################################################   
# Find out whether the shape is a cube
# But someone forgot to use proper record keeping, so we only have the volume, and the length of a single side! It's up to you to find out whether the cuboid has equal sides (= is a cube).

def cube_checker(volume, side):
    return volume > 0 and side > 0 and volume % (side**3) == 0

########################################################################################################################################################################   
# My head is at the wrong end!
# Save the animals by switching them back. You will be given an array which will have three values (tail, body, head). It is your job to re-arrange the array so that the animal is the right way round (head, body, tail).
  
def fix_the_meerkat(arr):
    arr.reverse()
    return arr 
  
########################################################################################################################################################################   
# Gravity Flip
# There are some columns of toy cubes in the box arranged in a line. The i-th column contains a_i cubes. At first, the gravity in the box is pulling the cubes downwards. When Bob switches the gravity, it begins to pull all the cubes to a certain side of the box, d, which can be either 'L' or 'R' (left or right). Below is an example of what a box of cubes might look like before and after switching gravity.

def flip(d, a):
    if d == "R":
        a.sort()
        return a
    else:
        a.sort(reverse = True)
        return a
  
########################################################################################################################################################################   
# Cat years, Dog years
# I got them at the same time as kitten/puppy. That was humanYears years ago. Return their respective ages now as [humanYears,catYears,dogYears]
  
def human_years_cat_years_dog_years(human_years):
    if human_years == 1:
        return [human_years, 15, 15]
    elif human_years == 2:
        return [human_years, 24, 24]
    else:
        return [human_years, 24 + (human_years-2)*4, 24 + (human_years-2)*5 ]  
  
########################################################################################################################################################################   
# Determine offspring sex based on genes XX and XY chromosomes
# Determine if the sex of the offspring will be male or female based on the X or Y chromosome present in the male's sperm.

def chromosome_check(sperm):
     if sperm == "XY":
        return 'Congratulations! You\'re going to have a son.'
     else:
        return 'Congratulations! You\'re going to have a daughter.'

########################################################################################################################################################################   
# altERnaTIng cAsE <=> ALTerNAtiNG CaSe
# Define String.prototype.toAlternatingCase (or a similar function/method such as to_alternating_case/toAlternatingCase/ToAlternatingCase in your selected language; see the initial solution for details) such that each lowercase letter becomes uppercase and each uppercase letter becomes lowercase. For example:

def to_alternating_case(string):
    les = list(string)
    y = list()
    for x in les:
        if x.isupper():
            y.append(x.lower())
        else:
            y.append(x.upper())
    return ''.join(y)


########################################################################################################################################################################   
# Convert a String to a Number!
# We need a function that can transform a string into a number

def string_to_number(s):
    return int(s)

########################################################################################################################################################################   
# Drink about
# Make a function that receive age, and return what they drink.

def people_with_age_drink(age):
    if age < 14: return "drink toddy"
    elif age < 18: return "drink coke"
    elif age < 21: return "drink beer"
    else: return "drink whisky"

########################################################################################################################################################################   
# How good are you really?
# You receive an array with your peers' test scores. Now calculate the average and compare your score! Return True if you're better, else False!

def better_than_average(class_points, your_points):
    if sum(class_points)/len(class_points) < your_points:
        return True
    else:
        return False

########################################################################################################################################################################   
# Fake Binary
# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

def fake_bin(x):
    les = list(x)
    ss = list()
    for x in les:
        x = int(x)
        if x < 5:
            ss.append("0")
        else:
            ss.append("1")
    return "".join(ss)

def fake_bin(x):
    return ''.join('0' if c < '5' else '1' for c in x)
  
########################################################################################################################################################################   
# Simple Fun #1: Seats in Theater
# Given the total number of rows and columns in the theater (nRows and nCols, respectively), and the row and column you're sitting in, return the number of people who sit strictly behind you and in your column or to the left, assuming all seats are occupied.

  def seats_in_theater(tot_cols, tot_rows, col, row):
    return (tot_cols - (col -1)) * (tot_rows - row)

########################################################################################################################################################################   
# Triple Trouble
# Create a function that will return a string that combines all of the letters of the three inputed strings in groups. Taking the first letter of all of the inputs and grouping them next to each other. Do this for every letter, see example below!

def triple_trouble(one, two, three):
    x = ""
    count = 0
    while count < len(one):
        x += one[count] + two[count] + three[count]
        count += 1
    return x
  
########################################################################################################################################################################   
# Never visit a . . . !?
# Complete the function which get an input number n such that n >= 10 and n < 10000, then:

def subtract_sum(number):
    return "apple"

########################################################################################################################################################################   
# Parse nice int from char problem
# Write a program that returns the girl's age (0-9) as an integer. Assume the test input string is always a valid string. For example, the test input may be "1 year old" or "5 years old". The first character in the string is always a number.

def get_age(age):
    return int(age[0])

########################################################################################################################################################################   
# Difference of Volumes of Cuboids
# In this simple exercise, you will create a program that will take two lists of integers, a and b. Each list will consist of 3 positive integers above 0, representing the dimensions of cuboids a and b. You must find the difference of the cuboids' volumes regardless of which is bigger.
  
def find_difference(a, b):
    x = 1
    y = 1
    for x1 in a:
        x = x1 * x
    for y1 in b:
        y = y1 * y
    return abs(x - y)    
  
########################################################################################################################################################################   
# Sum The Strings
# Create a function that takes 2 integers in form of a string as an input, and outputs the sum (also as a string):
  
def sum_str(a, b):
    try:
        return str(int(a) + int(b))
    except:
        if a == "":
            a = 0
        if b == "":
            b = 0
        return str(int(a) + int(b))
  
def sum_str(a, b):
    return str(int(a or 0) + int(b or 0))  
  
########################################################################################################################################################################   
# Basic variable assignment
# This code should store "codewa.rs" as a variable called name but it's not working. Can you figure out why?

a = "code"
b = "wa.rs"
name = a + b

########################################################################################################################################################################   
# Are You Playing Banjo?

def are_you_playing_banjo(name):
    if name[0] == "R" or  name[0] == "r": return name + " plays banjo" 
    else: return  name + " does not play banjo"

########################################################################################################################################################################   
# Remove exclamation marks
# Write function RemoveExclamationMarks which removes all exclamation marks from a given string.

def remove_exclamation_marks(s):
    les = list(s)
    x = ""
    count = 0
    for t in les:
        if t != "!":
            x += t
    return x

def remove_exclamation_marks(s):
    return s.replace('!', '')

########################################################################################################################################################################   
# Find Maximum and Minimum Values of a List
# Your task is to make two functions ( max and min, or maximum and minimum, etc., depending on the language ) that receive a list of integers as input, and return the largest and lowest number in that list, respectively.

def minimum(arr):
    return min(arr)

def maximum(arr):
    return max(arr)
  
########################################################################################################################################################################   
# Basic Mathematical Operations
# Your task is to create a function that does four basic mathematical operations.  
  
def basic_op(operator, value1, value2):
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "*":
        return value1 * value2
    else:
        return value1 / value2  
  
def basic_op(operator, value1, value2):
    return eval("{}{}{}".format(value1, operator, value2))  
  
  
########################################################################################################################################################################     
  # Return the day
  # Complete the function which returns the weekday according to the input number:
  
def whatday(num):
    if num < 1 or num > 7:
        return "Wrong, please enter a number between 1 and 7"
    d = {1 : "Sunday", 2 : "Monday", 3: "Tuesday", 4 : "Wednesday", 5 : "Thursday", 6 : "Friday", 7 : "Saturday"}
    return d.get(num)  
  
########################################################################################################################################################################     
# No Loops 2 - You only need one
# You will be given an array a and a value x. All you need to do is check whether the provided array contains the value, without using a loop.
# Array can contain numbers or strings. x can be either. Return true if the array contains the value, false if not. With strings you will need to account for case.

def check(a, x): 
    return x in a

########################################################################################################################################################################     
# Grasshopper - Debug
# Remember that typically temperatures in the current weather conditions are given in whole numbers. It is possible for temperature sensors to report temperatures with a higher accuracy such as to the nearest tenth. Instrument error though makes this sort of accuracy unreliable for many types of temperature measuring sensors.


def weather_info (temp):
    c = convert_to_celsius(temp)
    if (c < 0):
        return (str(c) + " is freezing temperature")
    else:
        return (str(c) + " is above freezing temperature")
    
def convert_to_celsius (temperature):
    celsius = ((temperature) - 32) * (5/9)
    return celsius

########################################################################################################################################################################     
# Remove duplicates from list
# Define a function that removes duplicates from an array of numbers and returns it as a result. The order of the sequence has to stay the same.

def distinct(seq):
    track = list()
    new = list()
    count = 0
    while count <= len(seq)-1:
        if seq[count] in track:
            count += 1
        else:
            new.append(seq[count])
            track.append(seq[count])
            count += 1
    return new

########################################################################################################################################################################     
# Is it even?
# Your code will determine if the number passed is even (or not). The function needs to return either a true or false.

def is_even(n): 
    return n % 2 == 0
  
########################################################################################################################################################################     
# N-th Power
# You are given an array with positive numbers and a non-negative number N. You should find the N-th power of the element in the array with the index N. If N is outside of the array, then return -1. Don't forget that the first element has the index 0.
  
 def index(array, n):
    try:
        return array[n]**n
    except:
        return -1 
  
########################################################################################################################################################################       
# Exclamation marks series #1: Remove an exclamation mark from the end of string
# Remove an exclamation mark from the end of a string. For a beginner kata, you can assume that the input data is always a string, no need to verify it.
  
def remove(s):
    if s.endswith("!"):
        return s[0:len(s)-1]
    else:
        return s
      
########################################################################################################################################################################            
# Basic Training: Add item to an Array
# Add the value "codewars" to the websites array.
      
websites.append("codewars")      
      
########################################################################################################################################################################      # get character from ASCII Valu 
# Write a function get_char() / getChar() which takes a number and returns the corresponding ASCII char for that value.
      
 def get_char(c):
    return chr(c)     
      
########################################################################################################################################################################                  
# Will you make it?
# Considering these factors, write a function that tells you if it is possible to get to the pump or not. Function should return true if it is possible and false if not.

def zero_fuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump - (mpg * fuel_left) <= 0 

########################################################################################################################################################################                  
# Safen User Input Part I - htmlspecialchars
# Your mission is to implement a function that converts the following potentially harmful characters:

def html_special_chars(data): 
    data = data.replace("&", "&amp;")
    data = data.replace("<", "&lt;")
    data = data.replace(">", "&gt;")
    data = data.replace("\"", "&quot;")
    return data

def html_special_chars(data): 
    return data.replace('&', "&amp;").replace('>', "&gt;").replace('<', "&lt;").replace('\"', "&quot;")

########################################################################################################################################################################                  
# String Templates - Bug Fixing #5
# Oh no! Timmy hasn't followed instructions very carefully and forgot how to use the new String Template feature, Help Timmy with his string template so it works as he expects!

def build_string(*args):
    return "I like {0}!".format(", ".join(args))
  
########################################################################################################################################################################                  
# Switch it Up!
# When provided with a number between 0-9, return it in words.

def switch_it_up(number):
    d = {1 : "One", 
             2 : "Two",
             3 : "Three",
             4 : "Four",
             5 : "Five",
             6 : "Six",
             7 : "Seven",
             8 : "Eight",
             9 : "Nine",
             0 : "Zero"}
    return d.get(number)

return ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine'][n]

########################################################################################################################################################################                  
# Grasshopper - Basic Function Fixer
# I created this function to add five to any number that was passed in to it and return the new value. It doesn't throw any errors but it returns the wrong number.

def add_five(num):
    return num + 5
  
########################################################################################################################################################################                  
# Keep up the hoop
# Alex just got a new hula hoop, he loves it but feels discouraged because his little brother is better than him
  
def hoop_count(n):
  return "Keep at it until you get it" if n < 10 else "Great, now move on to tricks"
  
########################################################################################################################################################################                  
# Grasshopper - Messi Goals
# Use variables to find the sum of the goals Messi scored in 3 competitions

la_liga_goals = 43
champions_league_goals = 10
copa_del_rey_goals = 5
total_goals = la_liga_goals + champions_league_goals + copa_del_rey_goals  
  
########################################################################################################################################################################                  
# Welcome!
# Write a 'welcome' function that takes a parameter 'language' (always a string), and returns a greeting - if you have it in your database. It should default to English if the language is not in the database, or in the event of an invalid input.

def greet(language):
    d = {'english': 'Welcome',
        'czech': 'Vitejte',
        'danish': 'Velkomst',
        'dutch': 'Welkom',
        'estonian': 'Tere tulemast',
        'finnish': 'Tervetuloa',
        'flemish': 'Welgekomen',
        'french': 'Bienvenue',
        'german': 'Willkommen',
        'irish': 'Failte',
        'italian': 'Benvenuto',
        'latvian': 'Gaidits',
        'lithuanian': 'Laukiamas',
        'polish': 'Witamy',
        'spanish': 'Bienvenido',
        'swedish': 'Valkommen',
        'welsh': 'Croeso'}
    return d.get(language,"Welcome")
  
########################################################################################################################################################################                  
# How many lightsabers do you own?
# Inspired by the development team at Vooza, write the function that accepts the name of a programmer, and returns the number of lightsabers owned by that person.
def how_many_light_sabers_do_you_own(name = None):
    if name == None: return 0
    if name == "Zach": return 18
    return 0   
    
########################################################################################################################################################################
# Multiply
# Fix the code so it works      
 def multiply(a, b):
    return a * b     
      
########################################################################################################################################################################
# Unfinished Loop - Bug Fixing #1
# Fix the bug in the unfinished loop

def create_array(n):
    res=[]
    i=1
    while i<=n: 
        res+=[i]
        i += 1
    return res
  
########################################################################################################################################################################
# Quarter of the year
# Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.

def quarter_of(month):
    d = {1: 1, 2:1, 3:1, 4:2, 5:2, 6:2, 7:3, 8:3, 9:3, 10:4, 11:4, 12:4}
    return d.get(month)

########################################################################################################################################################################
# The 'if' function
# Create a function called _if which takes 3 arguments: a value bool and 2 functions (which do not take any parameters): func1 and func2 When bool is truthy, func1 should be called, otherwise call the func2.

def _if(bool, func1, func2):
    if bool == True:
        return func1()
    else:
        return func2()

def _if(bool, func1, func2):
  func1() if bool else func2()

########################################################################################################################################################################
# Name on billboard
# You can print your name on a billboard ad. Find out how much it will cost you. Each character has a default price of £30, but that can be different if you are given 2 parameters instead of 1 (allways 2 for Java).

def billboard(name, price=30):
    total = 0
    for n in range(1,(len(name)+1)):
        total += price
    return total

########################################################################################################################################################################
# Welcome to the City
# Create a method that takes as input a name, city, and state to welcome a person. Note that name will be an array consisting of one or more values that should be joined together with one space between each, and the length of the name array in test cases will vary.

def say_hello(name, city, state):
    return f"Hello, {' '.join(name)}! Welcome to {city}, {state}!"

########################################################################################################################################################################
# Stringy Strings
# write me a function stringy that takes a size and returns a string of alternating 1s and 0s. the string should start with a 1.

def stringy(size):
    string = ""
    active = True
    for i in range(1, size + 1):
        if active:
            string += "1"
            active = False
        else:
            string += "0"
            active = True
    return string

########################################################################################################################################################################
# Double Char
# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

def double_char(s):
    x = ""
    for i in range(0, len(s)):
        x += s[i] * 2
    return x

def double_char(s):
    return ''.join(c * 2 for c in s)

########################################################################################################################################################################
# Remove First and Last Character Part Two
# Write a function which returns a new string containing the same character sequences except the first and the last ones but this time separated by spaces.

def array(string):
    if len(string) <= 4:
        return None
    else:
        s1 = string[string.find(",") + 1: string.rfind(",")].replace(",", " ").strip()
        if s1 == "":
            return None
        else:
            return s1

########################################################################################################################################################################
# Are they opposite?
# Give you two strings: s1 and s2. If they are opposite, return true; otherwise, return false. Note: The result should be a boolean value, instead of a string.
# The opposite means: All letters of the two strings are the same, but the case is opposite. you can assume that the string only contains letters or it's a empty string. Also take note of the edge case - if both strings are empty then you should return false/False.

def is_opposite(s1,s2):
    factor = True
    if s1 == "" or s2 == "":
        return False
    for i in range(0, len(s1)):
        if s1[i] != s2[i]:
            continue
        else:
            factor = False
            break
    return factor

########################################################################################################################################################################
# Printing Array elements with Comma delimiters
# Input: Array of elements Output: String with comma delimited elements of the array in th same order.

def print_array(arr):
    return ",".join(str(x) for x in arr)

########################################################################################################################################################################
# Job Matching #1
# create a function match (job_matching in Python) which takes a candidate and a job, which will return a Boolean indicating whether the job is a valid match for the candidate.

def job_matching(candidate, job):
    return candidate.get("min_salary")*0.9 <= job.get("max_salary")

########################################################################################################################################################################
# Miles per gallon to kilometers per liter
# Create an application that will display the number of kilometers per liter (output) based on the number of miles per imperial gallon (input).

def converter(mpg):
    return round((mpg * 1.609344 / 4.54609188), 2)

########################################################################################################################################################################
# Regex count lowercase letters
# Your task is simply to count the total number of lowercase letters in a string.

def lowercase_count(strng):
    total = 0
    for x in range(0, len(strng)):
        if strng[x].islower():
            total += 1
        else:
            continue
    return total

def lowercase_count(strng):
    return sum(a.islower() for a in strng)

########################################################################################################################################################################
# Draw stairs
# Given a number n, draw stairs using the letter "I", n tall and n wide, with the tallest in the top left.

def draw_stairs(n):
    output_string = ''
    for num in range(0,n-1):
        output_string += ' '*num + 'I\n'
    output_string +=  ' '*(n-1) + 'I'
    return output_string

########################################################################################################################################################################
# Total pressure calculation
# Calculate the total preesure of two molecules

def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp) :
    return ((given_mass1/molar_mass1 + given_mass2/molar_mass2) * (0.082) * (temp + 273.15))/volume

########################################################################################################################################################################
# Training JS #18: Methods of String object--concat() split() and its good friend join()
# Implement a function which accepts 2 arguments: string and separator.
# The expected algorithm: split the string into words by spaces, 
# split each word into separate characters and join them back with the specified separator, join all the resulting "words" back into a sentence with spaces.

def split_and_merge(string_, separator):
    str1 = string_.split(" ")
    x = ""
    for word in str1:
        ax = separator.join(word)
        x += " " + ax
    return x.strip()

########################################################################################################################################################################
# Sum of Multiples
# Find the sum of all multiples of n below m
def sum_mul(n, m):
    if n == 0 or m == 0:
        return "INVALID"
    elif n == m:
        return 0
    elif n < 0 or m < 0:
        return "INVALID"
    else:
        return sum(range(n, m, n))

########################################################################################################################################################################
# Who ate the cookie?
# For this problem you must create a program that says who ate the last cookie. If the input is a string then "Zach" ate the cookie. If the input is a float or an int then "Monica" ate the cookie. If the input is anything else "the dog" ate the cookie.

def cookie(x):
    if type(x) == str:
        return "Who ate the last cookie? It was Zach!"
    elif type(x) == int or type(x) == float:
        return "Who ate the last cookie? It was Monica!"
    else:
        return "Who ate the last cookie? It was the dog!"

########################################################################################################################################################################
# Who is going to pay for the wall?
# Your code will show Full name of the neighbor and the truncated version of the name as an array. If the number of the characters in name is less than or equal to two, it will return an array containing only the name as is"

def who_is_paying(name):
    return [name, name[0:2]] if len(name) >= 3 else [name]

########################################################################################################################################################################
# Grasshopper - Function syntax debugging
# A student was working on a function and made some syntax mistakes while coding. Help them find their mistakes and fix them.

def main (verb, noun):
    return verb + noun

########################################################################################################################################################################
# Holiday VIII - Duty Free
# The purpose of this kata is to work out just how many bottles of duty free whiskey you would have to buy such that the savings over the normal high street price would effectively cover the cost of your holiday.

import math
def duty_free(price, discount, holiday_cost):
    return math.floor(holiday_cost/((discount/100)*price))
    
########################################################################################################################################################################
# No zeros for heros
# Numbers ending with zeros are boring. They might be fun in your world, but not here. Get rid of them. Only the ending ones.

def no_boring_zeros(n):
    if n == 0:
        return 0
    n = str(n)
    val = 0
    for x in n[::-1]:
        if x == "0":
            val += 1
        else:
            break
    return int(n[0:len(n)-val])

def no_boring_zeros(n):
    try:
        return int(str(n).rstrip('0'))
    except ValueError:
        return 0

########################################################################################################################################################################
# Area or Perimeter
# You are given the length and width of a 4-sided polygon. The polygon can either be a rectangle or a square. If it is a square, return its area. If it is a rectangle, return its perimeter. 

def area_or_perimeter(l , w):
    return l * w if l == w else 2 * l + 2 * w
    
########################################################################################################################################################################
# Reverse List Order
# In this kata you will create a function that takes in a list and returns a list with the reverse order.

def reverse_list(l):
    l.reverse()
    return l

def reverse_list(l):
  return l[::-1]
########################################################################################################################################################################
# Will there be enough space?
# You have to write a function that accepts three parameters: If there is enough space, return 0, and if there isn't, return the number of passengers he can't take.

def enough(cap, on, wait):
    return 0 if cap >= on + wait else abs(on + wait - cap)

########################################################################################################################################################################
# Remove First and Last Character
# It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string. You're given one parameter, the original string. You don't have to worry with strings with less than two characters.

def remove_char(s):
    return s[1:len(s)-1]

########################################################################################################################################################################
# How much water do I need?
#

def how_much_water(water, load, clothes):
    if clothes > (2*load):
        return "Too much clothes"
    elif clothes < load:
        return "Not enough clothes"
    return float("%.2f" % (water * 1.1 ** (clothes - load)))
    
########################################################################################################################################################################
# Collatz Conjecture (3n+1)
# Your task is to make a function hotpo that takes a positive n as input and returns the number of times you need to perform this algorithm to get n = 1.

def hotpo(n):
    val = 0
    while n != 1:
        if n % 2 == 0:
            n = n / 2 
            val += 1
        else:
            val += 1
            n = n * 3 + 1
    return val

########################################################################################################################################################################
# Filter out the geese
#

geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    return [bird for bird in birds if bird not in geese]
    
########################################################################################################################################################################
# Training JS #7: if..else and ternary operator
# Complete function saleHotdogs/SaleHotDogs/sale_hotdogs, function accepts 1 parameter:n, n is the number of hotdogs a customer will buy, different numbers have different prices (refer to the following table), return how much money will the customer spend to buy that number of hotdogs.

def sale_hotdogs(n):
    if n < 5:
        return n * 100
    elif n < 10:
        return n * 95
    else:
        return n * 90

########################################################################################################################################################################
# Pythagorean Triple
# Given an unsorted array of 3 positive integers [ n1, n2, n3 ], determine if it is possible to form a Pythagorean Triple using those 3 integers.

def pythagorean_triple(integers):
    integers.sort()
    return integers[0]**2 + integers[1]**2 == integers[2]**2
    
########################################################################################################################################################################
# Alan Partridge II - Apple Turnover
# Your job is simple, if x squared is more than 1000, return It's hotter than the sun!!, else, return Help yourself to a honeycomb Yorkie for the glovebox.

def apple(x):
    return "It's hotter than the sun!!" if int(x)**2 > 1000 else "Help yourself to a honeycomb Yorkie for the glovebox."

########################################################################################################################################################################
# Count the Monkeys!
# Given the number (n), populate an array with all numbers up to and including that number, but excluding zero.

def monkey_count(n):
    return list(range(1, n+1))
    
########################################################################################################################################################################
# Check same case
# Write a function that will check if two given characters are the same case.

def same_ase(a, b): 
    if a.isalpha() and b.isalpha():
        if a.isupper() and b.isupper() or a.islower() and b.islower():
            return 1
        else:
            return 0
    else:
        return -1

########################################################################################################################################################################
# Crash Override
# Your task is to create a function that, given a proper first and last name, will return the correct alias.
def alias_gen(f_name, l_name):
    if f_name[0].isalpha() and l_name[0].isalpha():
        return f"{FIRST_NAME[f_name[0].upper()]} {SURNAME[l_name[0].upper()]}"
    else:
        return 'Your name must start with a letter from A - Z.'
########################################################################################################################################################################
# Count of positives / sum of negatives
# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

def count_positives_sum_negatives(arr):
    if not arr:
        return []
    negsum = 0
    possum = 0
    for x in arr:
        if x > 0:
            possum += 1
        else:
            negsum += x
    return [possum, negsum]

########################################################################################################################################################################
# You only need one - Beginner
# You will be given an array a and a value x. All you need to do is check whether the provided array contains the value. Array can contain numbers or strings. X can be either.

def check(seq, elem):
    active = False
    for x in seq:
        if x == elem:
            active = True
    return active

def check(seq, elem):
    return elem in seq
    
########################################################################################################################################################################
# Find the Remainder
# Write a function that accepts two integers and returns the remainder of dividing the larger value by the smaller value. Division by zero should return an empty value.

def remainder(a,b):
    try:
        if a >= b:
            return a % b
        else:
            return b % a
    except:
        return None
        
########################################################################################################################################################################
# Enumerable Magic - Does My List Include This?
# Create a method that accepts a list and an item, and returns true if the item belongs to the list, otherwise false.

def include(arr,item):
    return item in arr

########################################################################################################################################################################
# Sum Arrays
# Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative or non-integer. If the array does not contain any numbers then you should return 0.

def sum_array(a):
    try:
        return sum(a)
    except:
        return 0

########################################################################################################################################################################
# Beginner Series #4 Cockroach
# The cockroach is one of the fastest insects. Write a function which takes its speed in km per hour and returns it in cm per second, rounded down to the integer (= floored).

def cockroach_speed(s):
    return int(s*27.778)

########################################################################################################################################################################
# Pick a set of first elements
# Write a function to get the first element(s) of a sequence. Passing a parameter n (default=1) will return the first n element(s) of the sequence. If n == 0 return an empty sequence []

def first(seq, n = 1): 
    return seq[0:n]

########################################################################################################################################################################
# Sum of differences in array
# Your task is to sum the differences between consecutive pairs in the array in descending order.

def sum_of_differences(arr):
    if len(arr) <= 1:
        return 0
    else:
        arr.sort(reverse = True)
        return arr[0] - arr[-1]

########################################################################################################################################################################
# I love you, a little , a lot, passionately ... not at all
# Your goal in this kata is to determine which phrase the girls would say at the last petal for a flower of a given number of petals. The number of petals is always greater than 0.

def how_much_i_love_you(nb_petals):
    dict = {1 : "I love you", 2 : "a little", 3 : "a lot", 4 : "passionately", 5: "madly", 0 : "not at all"}
    return dict.get(nb_petals % 6)

########################################################################################################################################################################
# Multiplication table for number
# Your goal is to return multiplication table for number that is always an integer from 1 to 10.

def multi_table(number):
    string = ""
    for i in range(1,11):
        string += (f"{i} * {number} = {i*number}\n")
    return string.rstrip()

########################################################################################################################################################################
# Convert to Binary
# Given a non-negative integer n, write a function to_binary/ToBinary which returns that number in a binary format.

def to_binary(n):
    return int(str(bin(n))[2:])

########################################################################################################################################################################
# Grasshopper - Terminal game move function
# In this game, the hero moves from left to right. The player rolls the dice and moves the number of spaces indicated by the dice two times.
# Create a function for the terminal game that takes the current position of the hero and the roll (1-6) and return the new position.

def move(position, roll):
    return position + roll * 2

########################################################################################################################################################################
# Switch/Case - Bug Fixing #6
# Oh no! Timmy's evalObject function doesn't work. He uses Switch/Cases to evaluate the given properties of an object, can you fix timmy's function?

def eval_object(v):
    match v["operation"]:
        case "+":
            return v["a"] + v["b"]
        case "-":
            return v["a"] - v["b"]
        case "/":
            return v["a"] / v["b"]
        case "*":
            return v["a"] * v["b"]
        case "%":
            return v["a"] % v["b"]
        case "**":
            return v["a"] ** v["b"]
        case _:
            return 1

########################################################################################################################################################################
# Find the first non-consecutive number
# Your task is to find the first element of an array that is not consecutive.

def first_non_consecutive(arr):
    if arr == list(range(arr[0], arr[len(arr)-1])):
        return None
    else:
        for i in range(0,len(arr)-1):
            if arr[i+1] != arr[i]+1:
                return arr[i+1]

########################################################################################################################################################################
# The Wide-Mouthed frog!
# create complete the mouth_size method this method takes one argument animal which corresponds to the animal encountered by the frog. If this one is an alligator (case-insensitive) return small otherwise return wide.

def mouth_size(animal): 
    return "wide" if animal.lower() != "alligator" else "small"


########################################################################################################################################################################
# Find numbers which are divisible by given number
# Complete the function which takes two arguments and returns all numbers which are divisible by the given divisor. First argument is an array of numbers and the second is the divisor.

def divisible_by(numbers, divisor):
    return [x for x in numbers if x % divisor == 0]

########################################################################################################################################################################
# Sort and Star
# will be given a list of strings. You must sort it alphabetically (case-sensitive, and based on the ASCII values of the chars) and then return the first value.
# The returned value must be a string, and have "***" between each of its letters.
def two_sort(array):
    array.sort()
    string = ""
    for i in array[0]:
        string += i + "***"
    return string[0:len(string)-3]
  
def two_sort(lst):
    return '***'.join(min(lst))

########################################################################################################################################################################
# Convert a Number to a String!
# We need a function that can transform a number (integer) into a string.

def number_to_string(num):
    return str(num)

########################################################################################################################################################################
# Sum Mixed Array
# Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.Return your answer as a number.

def sum_mix(arr):
    sum = 0
    for i in arr:
        sum += int(i)
    return sum

def sum_mix(arr):
    return sum(int(n) for n in arr)
  
########################################################################################################################################################################
# Hex to Decimal
# Complete the function which converts hex number (given as a string) to a decimal number.

def hex_to_dec(s):
    return int(s, 16)

########################################################################################################################################################################
# Incorrect division method
# This method, which is supposed to return the result of dividing its first argument by its second, isn't always returning correct values. Fix it.

def divide_numbers(x,y):
    return x / y

########################################################################################################################################################################
# Return Two Highest Values in List
# In this kata, your job is to return the two distinct highest values in a list. If there're less than 2 unique values, return as many of them, as possible. The result should also be ordered from highest to lowest.

def two_highest(arg1):
    arg1 = list(set(arg1))
    arg1.sort(reverse = True)
    if len(arg1) > 2:
        return [arg1[0], arg1[1]]
    else:
        return arg1
        
########################################################################################################################################################################
# FIXME: Replace all dots
# The code provided is supposed replace all the dots . in the specified String str with dashes -

import re
def replace_dots(s):
    return re.sub("\.", "-", s)
    
########################################################################################################################################################################
# Is your period late?
# Return true if the number of days passed from last to today is greater than cycleLength. Otherwise, return false.

from datetime import *
def period_is_late(last,today,cycle_length):
    return last + timedelta(days = cycle_length) < today

########################################################################################################################################################################
# Classy Extentions
# Your task is to complete the Cat class which Extends Animal and replace the speak method to return the cats name + meows. e.g. 'Mr Whiskers meows.'

from preloaded import Animal

class Cat(Animal):
    def speak(self):
            return f"{self.name} meows."
        
########################################################################################################################################################################
# Unexpected parsing
# Function should return a dictionary/Object/Hash with "status" as a key, whose value can : "busy" or "available" depending on the truth value of the argument is_busy.
def get_status(is_busy):
    return {"status": ("available", "busy")[is_busy]}

########################################################################################################################################################################
# Grasshopper - Terminal Game #1
# In this first kata in the series, you need to define a Hero prototype to be used in a terminal game. The hero should have the following attributes:

class Hero(object):
    def __init__(self, name = 'Hero', position = '00', health = 100, damage = 5, experience = 0):
        self.name = name
        self.position = position
        self.health = health
        self.damage = damage
        self.experience = experience

########################################################################################################################################################################
# Regular Ball Super Ball
# Create a class Ball. Ball objects should accept one argument for "ball type" when instantiated. If no arguments are given, ball objects should instantiate with a "ball type" of "regular."

class Ball(object):
    def __init__(self, ball_type = "regular"):
        self.ball_type = ball_type

########################################################################################################################################################################
# CSV representation of array
# Create a function that returns the CSV representation of a two-dimensional numeric array.

def to_csv_text(array):
    string = ""
    for x in array:
        for y in x:
            string += str(y) + ","
        string = string[0: len(string)-1] + "\n"
    return string.rstrip()

########################################################################################################################################################################
# Byte me!
# Return byte size of an object
import sys
def total_bytes(object):
    return sys.getsizeof(object)

########################################################################################################################################################################
# Is there a vowel in there?
# Given an array of numbers, check if any of the numbers are the character codes for lower case vowels (a, e, i, o, u). If they are, change the array value to a string of that vowe

def is_vow(inp):
    for x in range(0, len(inp)):
        if inp[x] == 97:
            inp.pop(x)
            inp.insert(x, "a")
        if inp[x] == 101:
            inp.pop(x)
            inp.insert(x, "e")
        if inp[x] == 105:
            inp.pop(x)
            inp.insert(x, "i")
        if inp[x] == 111:
            inp.pop(x)
            inp.insert(x, "o")
        if inp[x] == 117:
            inp.pop(x)
            inp.insert(x, "u")
    return inp

def is_vow(inp):
    return [chr(n) if chr(n) in "aeiou" else n for n in inp]
########################################################################################################################################################################
# Classic Hello World
# You are given a method called main, make it print the line Hello World!, (yes, that includes a new line character at the end) and don't return anything. Make it print hello world

class Solution:
    def main(self):
        print("Hello World!")

########################################################################################################################################################################
# OOP: Object Oriented Piracy
#

class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
    def is_worth_it(self):
        return True if self.draft - self.crew * 1.5 > 20 else False

########################################################################################################################################################################
# Duck Duck Goose
# Task: Given an array of Player objects (an array of associative arrays in PHP) and an index (1-based), return the name of the chosen Player(name is a property of Player objects, e.g Player.name)

def duck_duck_goose(players, goose):
    return players[goose % len(players) - 1].name
########################################################################################################################################################################
# Beginner - Lost Without a Map
# Given an array of integers, return a new array with each value doubled.

def maps(a):
    return [x*2 for x in a]

########################################################################################################################################################################
# Calculate Price Excluding VAT
# Write a function that calculates the original product price, without VAT.

def excluding_vat_price(price):
    return -1 if price == None else round(price / 1.15, 2)

########################################################################################################################################################################
# Holiday VI - Shark Pontoon
#

def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    if dolphin:
        return "Alive!" if (pontoon_distance / you_speed < shark_distance / (shark_speed * 0.5)) else "Shark Bait!"
    else: 
        return "Alive!" if (pontoon_distance / you_speed < shark_distance / shark_speed) else "Shark Bait!"

########################################################################################################################################################################
# To square(root) or not to square(root)
# Return a new array with processing every number of the input-array like this:. If the number has an integer square root, take this, otherwise square the number.

import math
def square_or_square_root(arr):
    les = []
    for x in arr:
        if math.sqrt(x).is_integer():
            les.append(math.sqrt(x))
        else:
            les.append(x**2)
    return les
########################################################################################################################################################################
# Grasshopper - Grade book
# Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.

def get_grade(s1, s2, s3):
    avg = (s1 + s2 + s3) / 3
    if avg >= 90:
        return "A"
    if avg >= 80:
        return "B"
    if avg >= 70:
        return "C"
    if avg >= 60:
        return "D"
    else:
        return "F"

########################################################################################################################################################################
# Grasshopper - Personalized Message
# Create a function that gives a personalized greeting. This function takes two parameters: name and owner. Use conditionals to return the proper message:

def greet(name, owner):
    return "Hello boss" if name == owner else "Hello guest"

########################################################################################################################################################################
# Transportation on vacation
# 

def rental_car_cost(d):
    if d >= 7: 
        return d * 40 - 50
    elif d >= 3: 
        return d * 40 - 20
    else:
        return d*40

########################################################################################################################################################################
# Do I get a bonus?
# 

def bonus_time(salary, bonus):
    return f"${salary*10}" if bonus else f"${salary}"

########################################################################################################################################################################
# Get Planet Name By ID
# The function is not returning the correct values. Can you figure out why?

def get_planet_name(id):
    # This doesn't work; Fix it!
    name=""
    match id:
        case 1: name = "Mercury"
        case 2: name = "Venus"
        case 3: name = "Earth"
        case 4: name = "Mars"
        case 5: name = "Jupiter"
        case 6: name = "Saturn"
        case 7: name = "Uranus"  
        case 8: name = "Neptune"
    return name

########################################################################################################################################################################
# For Twins: 1. Types
# Write a function that will accept two parameters: variable and type and check if type of variable is matching type. Return true if types match or false if not.

########################################################################################################################################################################
# Fundamentals: Return
# Make multiple functions that will return the sum, difference, modulus, product, quotient, and the exponent respectively.

def add(a,b):
    return a + b

def multiply(a,b):
    return a * b
    
def  divide(a,b):
    return a / b

def  mod(a,b):
    return a % b

def exponent(a,b):
    return a ** b

def subt(a,b):
    return a - b

########################################################################################################################################################################
# Semi-Optional
# We have implemented a function wrap(value) that takes a value of arbitrary type and wraps it in a new JavaScript Object or Python Dict setting the 'value' key on the new Object or Dict to the passed-in value.

def wrap(value):
    return {"value":value}

########################################################################################################################################################################
# USD => CNY
# Create a function that converts US dollars (USD) to Chinese Yuan (CNY)

def usdcny(usd):
    x = format(usd * 6.75, ".2f")
    return f"{x} Chinese Yuan"

########################################################################################################################################################################
# Enumerable Magic #25 - Take the First N Elements
# Create a function that accepts a list/array and a number n, and returns a list/array of the first n elements from the list/array.

def take(arr,n):
    return arr[0:n]

########################################################################################################################################################################
# Hello, Name or World!
# Define a method hello that returns "Hello, Name!" to a given name, or says Hello, World! if name is not given (or passed as an empty String).

def hello(name = None):
    if name == "" or name == None:
        return "Hello, World!"
    else:
        return f"Hello, {name.title()}!"

########################################################################################################################################################################
# Pirates!! Are the Cannons ready!??
# 

def cannons_ready(gunners):
    for x in gunners.values():
        if x == "nay":
            return "Shiver me timbers!"
    return "Fire!"

########################################################################################################################################################################
# Count by X
# Create a function with two arguments that will return an array of the first n multiples of x.

def count_by(x, n):
    return list(range(x, x*n+1, x))

########################################################################################################################################################################
# Simple validation of a username with regex
# Write a simple regex to validate a username

def validate_usr(username):
    if len(username) < 4 or len(username) > 16:
        return False
    if username.lower() != username:
        return False
    if username.isalnum():
        return True
    if username.replace("_", "1").isalnum():
        return True
    else:
        return False
    

########################################################################################################################################################################
# Is this my tail?
#

def correct_tail(body, tail):
     return body[-1] == tail

########################################################################################################################################################################
# Merge two sorted arrays into one
# Complete the function mergeArrays(arr1, arr2), where arr1 and arr2 are the original sorted arrays.

def merge_arrays(arr1, arr2):
    a = list(set(arr1 + arr2))
    a.sort()
    return a
    
########################################################################################################################################################################
# Sum without highest and lowest number
# The highest or lowest element respectively is a single element at each edge, even if there are more than one with the same value.

def sum_array(arr):
    if arr == None or len(arr) == 0 or len(arr) == 1:
        return 0
    return sum(arr) - max(arr) - min(arr)

########################################################################################################################################################################
# Correct the mistakes of the character recognition software
#

def correct(s):
    return s.replace("5", "S").replace("0", "O").replace("1","I")

########################################################################################################################################################################
# How many stairs will Suzuki climb in 20 years?
# Your function should return the 20 year estimate of the stairs climbed using the formula above.

def stairs_in_20(stairs):
    i = 0
    for x in stairs:
        i += sum(x)
    return i * 20

########################################################################################################################################################################
# 101 Dalmatians - squash the bugs, not the dogs!
#

def how_many_dalmatians(n):
    if n == 101: 
        return  "101 DALMATIONS!!!" 
    elif n <= 10: 
        return "Hardly any"
    elif n < 51: 
        return "More than a handful!"
    else:
        return "Woah that's a lot of dogs!"

########################################################################################################################################################################
# Define a card suit
#

def define_suit(card):
    les = {"C": "clubs", "S" : "spades", "D" : "diamonds", "H" : "hearts"}
    return les.get(card[-1])

########################################################################################################################################################################
# Freudian translator
#

def to_freud(sentence):
    if sentence == "":
        return ""
    string = ""
    for x in sentence.rsplit(" "):
        string += "sex "
    return string.rstrip()

########################################################################################################################################################################
# Exclamation marks series #4: Remove all exclamation marks from sentence but ensure a exclamation mark at the end of string
# Remove all exclamation marks from sentence but ensure a exclamation mark at the end of string. For a beginner kata, you can assume that the input data is always a non empty string, no need to verify it.

def remove(s):
    return s.replace("!","") + "!"

########################################################################################################################################################################
# Exclamation marks series #2: Remove all exclamation marks from the end of sentence
# Remove all exclamation marks from the end of sentence.

def remove(s):
    while s.endswith("!"):
        s = s[0:len(s)-1]
    return s

def remove(s):
    return s.rstrip("!")

########################################################################################################################################################################
# Ensure question
# Given a string, write a function that returns the string with a question mark ("?") appends to the end, unless the original string ends with a question mark, in which case, returns the original string.

def ensure_question(s):
    return s if s.endswith("?") else s + "?"

########################################################################################################################################################################
# Filtering even numbers (Bug Fixes)
#

def kata_13_december(lst): 
    return [x for x in lst if x % 2 != 0]

########################################################################################################################################################################
# Flick Switch
# Create a function that always returns True for every item in a given list. However, if an element is the word "flick", switch to always returning the opposite boolean value.

def flick_switch(lst):
    les = []
    active = True
    for x in lst:
        if x =="flick":
            if active:
                active = False
            else:
                active = True
        les.append(active)
    return les

########################################################################################################################################################################
#
#

########################################################################################################################################################################
#
#

########################################################################################################################################################################
#
#

########################################################################################################################################################################
#
#

########################################################################################################################################################################
#
#

########################################################################################################################################################################
#
#

########################################################################################################################################################################
#
#

########################################################################################################################################################################
#
#

########################################################################################################################################################################








