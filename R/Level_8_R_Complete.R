library(tidyverse)
library(tidyr)
library(dplyr)
library(ggplot2)
library(tidyverse)
library(nycflights13)
library(Lahman)
library(ggstance)
library(lvplot)
library(ggbeeswarm)
library(heatmaply) 
library(hexbin)
library(modelr)
library(forcats)
library(stringr)
library(lubridate)


# Codewar Practice - Level 8 Kata
# All level 8 katas completed as of 4/10/23
#--------------------------------------------------------------------------------------------------------------------------------------------
# Cat years, Dog years
# I have a cat and a dog. I got them at the same time as kitten/puppy. That was humanYears years ago. Return their respective ages now as [humanYears,catYears,dogYears]

petyears <- function(humanYears){
  
  if(humanYears == 1)
  {
    catYears = 15
    dogYears = 15
    (Years <- c(humanYears, catYears, dogYears))
    Years
  }
  else if(humanYears == 2)
  {
    catYears = 24
    dogYears = 24
    (Years <- c(humanYears, catYears, dogYears))
  }
  else
  {
    catYears = 24 + (4 * (humanYears - 2))
    dogYears = 24 + (5 * (humanYears - 2))
    (Years <- c(humanYears, catYears, dogYears))
  }
}
#--------------------------------------------------------------------------------------------------------------------------------------------
# Simple multiplication
# This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.

simple_multiplication <- function(number) {
  if(number %% 2 == 0)
  {
    (number * 8)  
  }
  else
  {
    (number * 9)
  }
}
#--------------------------------------------------------------------------------------------------------------------------------------------
# Remove String Spaces
# Write a function that removes the spaces from the string, then return the resultant string.

no_space <- function(x) {
  str_replace_all(x, " ", "")
}

no_space("cats and dogs")
#--------------------------------------------------------------------------------------------------------------------------------------------
# String repeat
# Write a function that accepts an integer n and a string s as parameters, and returns a string of s repeated exactly n times.

repeat_string <- function(count, str) {
  str_dup(str,count )
}
repeat_string(3, "cat")
#--------------------------------------------------------------------------------------------------------------------------------------------
# Square sum
# Complete the square sum function so that it squares each number passed into it and then sums the results together. Ex. [1,2,2] would return 9

square_sum <- function(nums) {
  sum(nums1^2)
}

#--------------------------------------------------------------------------------------------------------------------------------------------
# Century 
# The first century spans from the year 1 up to and including the year 100, the second century - from the year 101 up to and including the year 200, etc.

century <- function(year) {
  x = year %/% 100 + 1
}
#--------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Create a function that takes an integer as an argument and returns "Even" for even numbers of "Odd" for odd numbers
# The best way to determine if an integer is using the special division operators %% and %/% 
# %% when used to divide a number will return the remainder that is left over. 4%%2 = 0 while 5%%2 = 1
# %/% when used to divide a number will return the quotient. 4%/%2 = 2 while 5%/%2 = 2
# Thus all we have to do is divide our number by %% and see if there is a remainder left. If there isn't then the number is even but if it is than then number is odd in all cases

EOO <- function(x){
  y = x%%2
  if(y == 0){
    "Even"
  } else {
    "Odd"
  }
}
EOO(1) # Returns "Odd"
EOO(2) # Returns "Even"
EOO(121) # Returns "Odd"
EOO(1000000) # Returns "Even"
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Is n divisible by x and y?
# Create a function that checks if a number n is divisible by two numbers x AND y. All inputs are positive, non-zero numbers.

is_divisible <- function(n, x, y) {
  ifelse(n%%x == 0 && n%%y == 0, TRUE , FALSE )
}
is_divisible(4,2,1)
is_divisible(3,3,4)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Even or Odd
# Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

even_or_odd <- function(n) {
  ifelse(n%%2 == 0, "Even", "Odd")
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Reversed Strings
# Complete the solution so that it reverses the string passed into it.
solution <- function(s){
  letters <- strsplit(s, NULL)[[1]]
  reversed <- paste(rev(letters), collapse="")
  reversed
}
solution("cat")
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Convert a Boolean to a String
# Implement a function which convert the given Boolean value into its string representation.

boolean_to_string <- function(b){
  (as.character(b))
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Quarter of the year
# Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.
# For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter; and month 11 (November), is part of the fourth quarter.
# Constraint: 1 <= month <= 12

quarter_of <- function(month){
  switch(month, 1,1,1,2,2,2,3,3,3,4,4,4)
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Third Angle of a Triangle
# Write a function to return the 3rd.

other_angle <- function(a, b){
  (x = 180 - a - b)
}
other_angle(50,60)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Reversed Words
# Complete the solution so that it reverses all of the words within the string passed in. Words are separated by exactly one space and there are no leading or trailing spaces
# Example: "The greatest victory is that which requires no battle" --> "battle no requires which that is victory greatest The"

solution <- function(sentence){
  sentence %>% str_split( " ") %>% unlist() %>% rev() %>% str_c(collapse = " ")
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Keep Hydrated!
# Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling. You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest value.
# time = 3 ----> litres = 1, time = 6.7---> litres = 3, time = 11.8--> litres = 5

litres <- function(time) {
  (time %/% 2)
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Filter out the geese
# Write a function that takes a list of strings as an argument and returns a filtered list containing the same elements but with the 'geese' removed.
# The geese are any strings in the following array, which is pre-populated in your solution: ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
# For example, if this array were passed as an argument:  ["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]
# Your function would return the following array: ["Mallard", "Hook Bill", "Crested", "Blue Swedish"]
# The elements in the returned array should be in the same order as in the initial array passed to your function, albeit with the 'geese' removed. Note that all of the strings will be in the same case as those provided, and some elements may be repeated.

goose_filter <- function(birds){
  birds[! birds %in% c("African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher")]
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Beginner Series #2 Clock
# Your task is to write a function which returns the time since midnight in milliseconds.
# h = 0, m = 1, s = 1 result = 61000

past <- function(h, m, s) {
  Msec = h * 3600000 + m * 60000 + s * 1000
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Invert values
# Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.
# Example: invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]

invert <- function(vec){
  -vec
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Beginner - Reduce but Grow
# Given a non-empty array of integers, return the result of multiplying the values together in order. Example: [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24

grow <- function(arr) {
  prod(arr)
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Grasshopper - Summation
# Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.

summation <- function(n) {
  sum(c(1:n))
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Remove exclamation marks 
# Write a function which removes all exclamation marks from a given string.

remove_exclamation_marks <- function(s){
  str_replace_all(s, "!", "")
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Find Maximum and Minimum Values of a List
# Your task is to make two functions ( max and min, or maximum and minimum, etc., depending on the language ) that receive a list of integers as input, and return the largest and lowest number in that list, respectively.
minimum <- function(vec){
  min(vec)
} 

maximum <- function(vec){
  max(vec)
} 
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Convert a String to a Number!

string_to_number <- function(x){
  as.double(x)
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Will you make it?
# You were camping with your friends far away from home, but when it's time to go back, you realize that your fuel is running out and the nearest pump is 50 miles away! You know that on average, your car runs on about 25 miles per gallon. There are 2 gallons left.
# Considering these factors, write a function that tells you if it is possible to get to the pump or not. Function should return true if it is possible and false if not.

zero_fuel <- function(distance, mpg, fuel_left) {
  ifelse(distance <= mpg * fuel_left, TRUE, FALSE)
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Difference of Volumes of Cuboids
# In this simple exercise, you will create a program that will take two lists of integers, a and b. Each list will consist of 3 positive integers above 0, representing the dimensions of cuboids a and b. You must find the difference of the cuboids' volumes regardless of which is bigger.
# For example, if the parameters passed are ([2, 2, 3], [5, 4, 1]), the volume of a is 12 and the volume of b is 20. Therefore, the function should return 8.

find_difference <- function(a, b){
  abs(prod(a)-prod(b))
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Calculate BMI
# Write function bmi that calculates body mass index (bmi = weight / height2).Write function bmi that calculates body mass index (bmi = weight / height2).
# if bmi <= 18.5 return "Underweight"
# if bmi <= 25.0 return "Normal"
# if bmi <= 30.0 return "Overweight"
# if bmi <= 30.0 return "Overweight"

bmi <- function(weight, height) {
  bmi = weight/(height^2)
  if(bmi <= 18.5) "Underweight"
  else if(bmi <= 25) "Normal"
  else if(bmi <= 30) "Overweight"
  else "Obese"
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Switch it Up!
# When provided with a number between 0-9, return it in words.
# Input :: 1 Output :: "One".

switch_it_up <- function(number){
  if(number == 0) "Zero"
  else(switch(number, "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"))
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Keep up the Hoop
#Write a program where Alex can input (n) how many times the hoop goes round and it will return him an encouraging message 
# If he doesn't get 10 hoops, return the string "Keep at it until you get it".

hoop_count <- function(n){
  ifelse(n >= 10, "Great, now move on to tricks", "Keep at it until you get it")
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Opposites Attract
# Timmy & Sarah think they are in love, but around where they live, they will only know once they pick a flower each. If one of the flowers has an even number of petals and the other has an odd number of petals it means they are in love.
# Write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't

lovefunc <- function(flower1, flower2){
  ifelse((flower1+flower2) %% 2 != 0, TRUE, FALSE)
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Remove First and Last Character
# It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string. You're given one parameter, the original string. You don't have to worry with strings with less than two characters.

removeChar <- function(str){
  str_sub(str, 2, str_length(str)-1)
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Get the mean of an array
# Return the average of the given array rounded down to its nearest integer.

get_average <- function(marks){
  floor(mean(marks))
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Are You Playing Banjo?
# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!
# The function takes a name as its only argument, and returns one of the following strings:

are_you_playing_banjo <- function(name){
  FL <- str_sub(name, 1, 1)
  ifelse(FL == "R" | FL == "r", str_c(name, " plays banjo"), str_c(name, " does not play banjo"))
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Apple Turnover
# Your job is simple, if x squared is more than 1000, return It's hotter than the sun!!, else, return Help yourself to a honeycomb Yorkie for the glovebox.

apple <- function(x){
  x <- as.numeric(x)
  ifelse((x^2) > 1000, "It's hotter than the sun!!", "Help yourself to a honeycomb Yorkie for the glovebox.")
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Thinkful - Logic Drills: Traffic light
# You're writing code to control your town's traffic lights. You need a function to handle each change from green, to yellow, to red, and then to green again.
# Complete the function that takes a string as an argument representing the current state of the light and returns a string representing the state the light should change to.
# For example, when the input is green, output should be yellow.

update_light <- function(current){
  if(current == "green") "yellow"
    else if (current == "yellow") "red"
      else("green")
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# You Can't Code Under Pressure #1
# Code as fast as you can! You need to double the integer and return it.

double_integer <- function(i) {
  i*2
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Count the Monkeys!
# You take your son to the forest to see the monkeys. You know that there are a certain number there (n), but your son is too young to just appreciate the full number, he has to start counting them from 1.

monkey_count <- function(n) {
  (vc <- seq(1, n, 1))
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Basic Mathematical Operations
# The function should take three arguments - operation(string/char), value1(number), value2(number). The function should return result of numbers after applying the chosen operation.

basic_op <- function(operator, value1, value2){
  switch(operator,
         "+" = value1 + value2,
         "-" = value1 - value2,
         "*" = value1 * value2,
         "/" = value1 / value2
  )
}
basic_op("/", 2, 2)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# You only need one - Beginner
# You will be given an array a and a value x. All you need to do is check whether the provided array contains the value. Array can contain numbers or strings. X can be either.
# Return true if the array contains the value, false if not.

check <- function(a, x){
  if(!is.na(match(x,a)) & match(x, a) >= 1) TRUE 
  else FALSE
}

check2 <- function(a, x){
  x %in% a
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Count Odd Numbers below n
# Given a number n, return the number of positive odd numbers below n, EASY!
# 15 -> 7 (because odd numbers below 15 are [1, 3, 5, 7, 9, 11, 13])

odd_count <- function(n) {
  ifelse(n%%2 == 0, n/2, (n-1)/2)
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# MakeUpperCase
# Write a function which converts the input string to uppercase.

makeUpperCase <- function(s) {
  str_to_upper(s)
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Write a function which calculates the average of the numbers in a given list.

find_average <- function(vec){
  ifelse(length(vec) == 0, 0, sum(vec)/length(vec))
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Will there be enough space?
# You have to write a function that accepts three parameters: cap is the amount of people the bus can hold excluding the driver.
# on is the number of people on the bus excluding the driver.
# wait is the number of people waiting to get on to the bus excluding the driver.
# If there is enough space, return 0, and if there isn't, return the number of passengers he can't take.

enough <- function(cap, on, wait){
  ifelse(cap >= on + wait, 0, abs(on+wait-cap))
}

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Holiday VIII - Duty Free
# The purpose of this kata is to work out just how many bottles of duty free whiskey you would have to buy such that the saving over the normal high street price would effectively cover the cost of your holiday.
# You will be given the high street price (normPrice), the duty free discount (discount) and the cost of the holiday.
# For example, if a bottle cost £10 normally and the discount in duty free was 10%, you would save £1 per bottle. If your holiday cost £500, the answer you should return would be 500.
# All inputs will be integers. Please return an integer. Round down.

duty_free <- function(price, discount, holiday_cost){
  x = (discount)/100
  y = (price * x)
  floor(holiday_cost/y)
}

duty_free(12, 50, 1000)
duty_free(17, 10, 500)
duty_free(24, 35, 3000)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Return Negative
# In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?

make_negative <- function(num){
  -abs(num)
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Twice as old
# Your function takes two arguments:
# current father's age (years)
# current age of his son (years)
# Сalculate how many years ago the father was twice as old as his son (or in how many years he will be twice as old). The answer is always greater or equal to 0, no matter if it was in the past or it is in the future.

twice_as_old <- function(dad_years_old, son_years_old){
  abs(dad_years_old - (son_years_old*2))
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Beginner - Lost Without a Map
# Given an array of integers, return a new array with each value doubled.

maps <- function(v) {
  v*2
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Beginner Series #4 Cockroach
# rite a function which takes its speed in km per hour and returns it in cm per second, rounded down to the integer (= floored).

cockroach_speed <- function(s){
  floor(s*27.778)
}

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# What's the real floor?
# Write a function that given a floor in the american system returns the floor in the european system.
# With the 1st floor being replaced by the ground floor and the 13th floor being removed, the numbers move down to take their place. In case of above 13, they move down by two because there are two omitted numbers below them.
# Basements (negatives) stay the same as the universal level.

get_real_floor <- function(n){
  if(n == 0) 0
  else if(n < 0) n
  else if(n == 1) 0
  else if(n == 15) 13
  else if(n == 14) 12
  else if(n > 15) n-2
  else  n-1
}

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Sum Arrays
# Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative or non-integer. If the array does not contain any numbers then you should return 0.

sum_array <- function(a){
  ifelse(length(a) == 0, 0, sum(a))
}

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# I love you, a little , a lot, passionately ... not at all
# If there are more than 6 petals, you start over with "I love you" for 7 petals, "a little" for 8 petals and so on.
# Your goal in this kata is to determine which phrase the girls would say at the last petal for a flower of a given number of petals. The number of petals is always greater than 0.


how_much_i_love_you <- function(nbpetals){
  x <- c("I love you", "a little", "a lot", "passionately", "madly", "not at all")
  if(nbpetals <= 6) x[nbpetals]
  else if(nbpetals %% 6 == 0) "not at all"
  else (x[nbpetals%%6])
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# My head is at the wrong end!
#  You will be given an array which will have three values (tail, body, head). It is your job to re-arrange the array so that the animal is the right way round (head, body, tail).

fix_the_meerkat <- function(vec){
  rev(vec)
}

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Gravity Flip
# There are some columns of toy cubes in the box arranged in a line. The i-th column contains a_i cubes. At first, the gravity in the box is pulling the cubes downwards. When Bob switches the gravity, it begins to pull all the cubes to a certain side of the box, d, which can be either 'L' or 'R' (left or right). Below is an example of what a box of cubes might look like before and after switching gravity.
# Given the initial configuration of the cubes in the box, find out how many cubes are in each of the n columns after Bob switches the gravity.

flip <- function(d, a){
  if(d == "R") sort(a) 
  else rev(sort(a))
}

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Expressions Matter
# Given three integers a ,b ,c, return the largest number obtained after inserting the following operators and brackets: +, *, ()
# In other words , try every combination of a,b,c with [*+()] , and return the Maximum Obtained

expression_matter <- function(a, b, c) {
  x <- a * (b + c)
  y <- (a + b) * c
  z <- a * b * c
  q <- a + b + c
  max(c( x, y, z, q))
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Terminal game move function
# In this game, the hero moves from left to right. The player rolls the dice and moves the number of spaces indicated by the dice two times.
# Create a function for the terminal game that takes the current position of the hero and the roll (1-6) and return the new position.

move <- function(pos, roll) {
  pos + roll * 2
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Pillars
# There are pillars near the road. The distance between the pillars is the same and the width of the pillars is the same. Your function accepts three arguments:
# number of pillars (≥ 1);
# distance between pillars (10 - 30 meters);
# width of the pillar (10 - 50 centimeters).
# Calculate the distance between the first and the last pillar in centimeters (without the width of the first and last pillar).

pillars = function(num_of_pillars, distance, width) {
  if(num_of_pillars < 2 ) 0
  else distance * (num_of_pillars - 1) * 100 + width * (num_of_pillars - 2)
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# DNA to RNA Conversion
# Deoxyribonucleic acid, DNA is the primary information storage molecule in biological systems. It is composed of four nucleic acid bases Guanine ('G'), Cytosine ('C'), Adenine ('A'), and Thymine ('T').
# Ribonucleic acid, RNA, is the primary messenger molecule in cells. RNA differs slightly from DNA its chemical structure and contains no Thymine. In RNA Thymine is replaced by another nucleic acid Uracil ('U').
# Create a function which translates a given DNA string into RNA.

dna_to_rna <- function(dna){
  gsub("T", "U", dna)
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Convert boolean values to strings 'Yes' or 'No'.
# Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.

bool_to_word <- function(bool){
  ifelse(bool, "Yes", "No")
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Returning Strings
# Make a function that will return a greeting statement that uses an input; your program should return, "Hello, <name> how are you doing today?".

greet <- function(name) {
  
}

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# The Wide-Mouthed frog!
# The wide-mouth frog is particularly interested in the eating habits of other creatures.
# He just can't stop asking the creatures he encounters what they like to eat. But, then he meets the alligator who just LOVES to eat wide-mouthed frogs!
# When he meets the alligator, it then makes a tiny mouth.
# Your goal in this kata is to create complete the mouth_size method this method takes one argument animal which corresponds to the animal encountered by the frog. If this one is an alligator (case-insensitive) return small otherwise return wide.

mouth_size <- function(animal){
  ifelse(tolower(animal) == "alligator", "small", "wide")
}

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Grasshopper - Messi goals function
# Complete the function to return his total number of goals in all three leagues.

goals <- function(la_liga_goals, copa_del_rey_goals, champions_league_goals) {
  la_liga_goals + copa_del_rey_goals + champions_league_goals
}

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Grasshopper - Grade book
# Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.

get_grade <- function(a, b, c){
  x <- sum(a,b,c)/3
  if(x >= 90) "A"
  else if(x >= 80) "B"
  else if(x >= 70) "C"
  else if(x >= 60) "D"
  else "F"
}

get_grade(70, 70, 100)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Beginner Series #1 School Paperwork
# Your classmates asked you to copy some paperwork for them. You know that there are 'n' classmates and the paperwork has 'm' pages. Your task is to calculate how many blank pages do you need. If n < 0 or m < 0 return 0.

paperwork <- function(n, m){
  if(n < 0 | m < 0) 0
  else n*m
}

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Array plus array
# get the sum of two arrays

array_plus_array <- function(vec1,vec2){
  sum(vec1) + sum(vec2)
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Grasshopper - Personalized Message
# Create a function that gives a personalized greeting. This function takes two parameters: name and owner. Use conditionals to return the proper message:

greet <- function(name, owner){
  ifelse(name == owner, "Hello boss", "Hello guest")
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Transportation on vacation
# Every day you rent the car costs $40. If you rent the car for 7 or more days, you get $50 off your total. Alternatively, if you rent the car for 3 or more days, you get $20 off your total. Write a code that gives out the total amount for different days(d).

rental_car_cost <- function(d){
  if(d >= 7) d * 40 - 50
  else if(d >= 3) d * 40 - 20
  else d*40
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Grasshopper - Check for facto
# This function should test if the factor is a factor of base. Return true if it is a factor or false if it is not.

check_for_factor <- function(base, factor) {
  ifelse(base %% factor == 0, TRUE, FALSE)
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Opposite number
# Very simple, given an integer or a floating-point number, find its opposite.

opposite <- function(number){
  -number
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Count by X
# Create a function with two arguments that will return an array of the first n multiples of x. Assume both the given number and the number of times to count will be positive numbers greater than 0. Return the results as an array or list ( depending on language ).

count_by <- function(x, n){
  seq(x, x*n, x)
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Subtract the Sum
# Complete the function which get an input number n such that n >= 10 and n < 10000, then:
# Sum all the digits of n.
# Subtract the sum from n, and it is your new n.
# If the new n is in the list below return the associated fruit, otherwise return back to task 1.

subtract_sum <- function(n) {
  fruits <- c("kiwi", "pear", "kiwi", "banana", "melon","banana", "melon", "pineapple", "apple")
  if(n <= 9 )
    fruits[n]
  else "apple"
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Convert number to reversed array of digits
# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.
# 35231 => [1,3,2,5,3]

digitize <- function(n){
  as.numeric(rev(str_extract_all(n, "", simplify = TRUE)))
}

digitize(35231)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Short Long Short
# Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. The strings will not be the same length, but they may be empty ( zero length ).
solution <- function(a, b) {
  ifelse(nchar(a) < nchar(b), paste(c(a,b,a), collapse = ""), paste(c(b,a,b), collapse = "") )
}

str_c(c("Cat", "Marsey"), collapse = "") # Same code

paste(c("Marsey", "cat"), collapse = "") # Same code

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Sum of positive
# You get an array of numbers, return the sum of all of the positives ones.
# Example [1,-4,7,12] => 1 + 7 + 12 = 20. If there is nothing to sum, then sum if default to 0

positive_sum <- function(vec){
  n <- 0
  for(x in seq_along(vec))
  {
    if(vec[[x]] >= 0)
      n <- n + vec[[x]]
  }
  n
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Double Char
# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.
# "String" -> "SSttrriinngg"

double_char <- function(str){
  nstr <- unlist(str_extract_all(str, ""))
  dbstr <- vector("character", length(nstr)*2)
  n <- 1
  for(x in seq_along(nstr))
  {
    dbstr[[n]] <- nstr[x]
    dbstr[[n+1]] <- nstr[x]
    n <- n+2 
  }
  str_c(dbstr, collapse = "")
}

double_char <- function(str){
  paste(rep(strsplit(str, "")[[1]], each = 2), collapse="") 
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Convert a Number to a String!
# Create a function that can transform a number (integer) into a string.

number_to_string <- function(n) {
  as.character(n)
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Sum Mixed Array
# Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

sum_mix <- function(vec){
  sum(as.numeric(vec))
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Get Nth Even Number
# Return the Nth Even Number

nth_even <- function(n) {
  n*2-2
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# get character from ASCII Value
# Write a function get_char() / getChar() which takes a number and returns the corresponding ASCII char for that value.
# get_char(65) should return "A"

get_char<- function(asc){
  intToUtf8(asc)
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Is this my tail?
# Some new animals have arrived at the zoo. The zoo keeper is concerned that perhaps the animals do not have the right tails. To help her, you must correct the broken function to make sure that the second argument (tail), is the same as the last letter of the first argument (body) - otherwise the tail wouldn't fit!
# If the tail is right return true, else return false.
# The arguments will always be non empty strings, and normal letters.

correct_tail <- function(body, tail){
  ifelse(str_sub(body, str_length(body)) == tail, TRUE, FALSE)
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Fake Binary
# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

fake_bin <- function(x){
  vec <- as.numeric(unlist(strsplit(x, "")))
  for(x in seq_along(vec))
  {
    if(vec[x] < 5) vec[x] <- "0"
    else vec[x] <- "1"
  }
  paste(vec, collapse = "")
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Find the smallest integer in the array
# Given an array of integers your solution should find the smallest integer.

findSmallestInt <- function(arr){
  min(arr) 
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Capitalization and Mutability
#  Fix the helper function they wrote so that it works as intended (i.e. make the first character in the string "word" upper case).

capitalize_word <- function(word){
  str_to_title(word)
}

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Century From Year
# Given a year, return the century it is in.

century <- function(year) {
  if(year <= 100) 1
  else if(year %% 100 == 0) year %/% 100 
  else year %/% 100 + 1
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Abbreviate a Two Word Name
# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

library(tidyverse)
abbrev_name <- function(name){
  x <- abbreviate(name,1, method = "both")
  y <- str_to_upper(x)
  z <- unlist(str_split(y, ""))
  str_c(z, collapse = ".")
}

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# IS there a vowel in there?
# Given an array of numbers, check if any of the numbers are the character codes for lower case vowels

# a = 97, e = 101, i = 105, o = 111, u = 117
is_vow <- function(a){
  for(x in seq_along(a))
  {
    if(a[x] == 97 ) a[x] <- "a"
    else if(a[x] == 101) a[x] <- "e"
    else if(a[x] == 105) a[x] <- "i"
    else if(a[x] == 111) a[x] <- "o"
    else if(a[x] == 117) a[x] <- "u"
    else a
  }
  a
}

is_vow <- function(x){
  sapply(x, function(v) ifelse(v %in% utf8ToInt("aeiou"), intToUtf8(v), v))
}

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Well of Ideas - Easy Version
# You need to check the provided array (x) for good ideas 'good' and bad ideas 'bad'. If there are one or two good ideas, return 'Publish!', if there are more than 2 return 'I smell a series!'. If there are no good ideas, as is often the case, return 'Fail!'.

well <- function(x){
  n <- sum(x == "good")
  if (n > 2 ) 'I smell a series!'
  else if(n > 0) 'Publish!'
  else "Fail!"
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Replace all dots
# Replace all the dots . in the specified String str with dashes -

replace_dots <- function(s){
  str_replace_all(s, "\\.", "-")
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Is he gonna survive?
# A hero is on his way to the castle to complete his mission. However, he's been told that the castle is surrounded with a couple of powerful dragons! each dragon takes 2 bullets to be defeated, our hero has no idea how many bullets he should carry.. Assuming he's gonna grab a specific given number of bullets and move forward to fight another specific given number of dragons, will he survive?

hero <- function(bullets, dragons) {
  ifelse(bullets >= dragons*2, TRUE, FALSE)
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# L1: Set alarm
# Write a function named setAlarm which receives two parameters. The first parameter, employed, is true whenever you are employed and the second parameter, vacation is true whenever you are on vacation.
# The function should return true if you are employed and not on vacation (because these are the circumstances under which you need to set an alarm). It should return false otherwise. Examples:

set_alarm <- function(employed, vacation) {
  ifelse( employed == TRUE & vacation == FALSE, TRUE, FALSE)
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# If you can't sleep, just count sheep!!
# Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers.

count_sheep <- function(n){
  vec <- vector("character", length = n)
  for(i in seq_along(vec))
  {
    ccc <- paste(i, "sheep...", collapse = "")
    vec[[i]] <- ccc
  }
  paste(vec, collapse = "")
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Convert a string to an array
# Write a function to split a string and convert it into an array of words.

string_to_array <- function(s){
  x <- unlist(strsplit(s, " "))
}

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Sort and Star
# You will be given a list of strings. You must sort it alphabetically (case-sensitive, and based on the ASCII values of the chars) and then return the first value. The returned value must be a string, and have "***" between each of its letters.
two_sort <- function(s){
  paste(unlist(strsplit(sort(s)[[1]], "")), collapse = "***")
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Rock Paper Scissors!
rps <- function(p1, p2){
  if(p1 == p2) "Draw!"
  else if(p1 == "rock" & p2 != "paper") "Player 1 won!"
  else if(p1 == "rock" & p2 == "paper") "Player 2 won!"
  else if(p1 == "scissors" & p2 != "paper") "Player 2 won!"
  else if(p1 == "scissors" & p2 == "paper") "Player 1 won!"
  else if(p1 == "paper" & p2 != "scissors") "Player 1 won!"
  else "Player 2 won!"
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Correct the mistakes of the character recognition software
# Character recognition software is widely used to digitize printed texts. Thus the texts can be edited, searched and stored on a computer.
# When documents (especially pretty old ones written with a typewriter), are digitized character recognition software often make mistakes.
# Your task is correct the errors in the digitized text. You only have to handle the following mistakes:
# S is misinterpreted as 5
# O is misinterpreted as 0
# I is misinterpreted as 1

correct <- function(string){
  string <- str_replace_all(string, "5", "S")
  string <- str_replace_all(string, "0", "O")
  string <- str_replace_all(string, "1", "I")
  print(string)
}

correct <- function(string){
  gsub('0', 'O',
       gsub('5', 'S',
            gsub('1', 'I', string)))
}
  
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 101 Dalmatians - squash the bugs, not the dogs!
# The expected behaviour is as follows:
# - Your friend has fewer than 10 dogs:                    "Hardly any"
# - Your friend has at least 10 but fewer than 51 dogs:    "More than a handful!"
# - Your friend has at least 51 but not exactly 101 dogs:  "Woah that's a lot of dogs!"
# - Your friend has 101 dogs:                              "101 DALMATIANS!!!"
# Your friend will always have between 1 and 101 dogs, inclusive.
  
how_many_dalmatians <- function(n) {
  if (n == 101) { "101 DALMATIANS!!!" }
  else if (n <= 10) {"Hardly any"} 
  else if (n < 51) {"More than a handful!"}
  else "Woah that's a lot of dogs!"
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Sentence Smash
# Write a function that takes an array of words and smashes them together into a sentence and returns the sentence. You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word.

smash <- function(words){
  paste(words, collapse = " ")
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Sum of Multiples
# Find the sum of all multiples of n below m

sum_mul <- function(n, m){
  if(n <= 0 | m <= 0 ) "INVALID"
  else if(n == m) 0
  else if (n > m) 0
  else if(m %% n == 0 ) sum(seq(from = n, to = m-n, by = n))
  else sum(seq(from = n, to = m, by = n))
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Student's Final Grade
# Create a function finalGrade, which calculates the final grade of a student depending on two parameters: a grade for the exam and a number of completed projects.
# This function should take two arguments: exam - grade for exam (from 0 to 100); projects - number of completed projects (from 0 and above); This function should return a number (final grade). There are four types of final grades:
# 100, if a grade for the exam is more than 90 or if a number of completed projects more than 10.
# 90, if a grade for the exam is more than 75 and if a number of completed projects is minimum 5.
# 75, if a grade for the exam is more than 50 and if a number of completed projects is minimum 2.
# 0, in other cases

final_grade <- function(exam, projects){
  if(exam > 90 | projects > 10) 100
  else if(exam > 75 & projects >= 5) 90
  else if(exam > 50 & projects >= 2 ) 75
  else 0
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 8kyu interpreters: HQ9+
# You task is to implement an simple interpreter for the notorious esoteric language HQ9+ that will work for a single character input:
# If the input is 'H', return 'Hello World!'
# If the input is 'Q', return the input
# If the input is '9', return the full lyrics of 99 Bottles of Beer. It should be formatted like this:

hq9 <- function(code) 
{
  if(code == "H" )"Hello World!"
  else if(code == "Q") "Q"
  else if(code == 9) "99 bottles of beer on the wall, 99 bottles of beer.\nTake one down and pass it around, 98 bottles of beer on the wall.\n98 bottles of beer on the wall, 98 bottles of beer.\nTake one down and pass it around, 97 bottles of beer on the wall.\n97 bottles of beer on the wall, 97 bottles of beer.\nTake one down and pass it around, 96 bottles of beer on the wall.\n96 bottles of beer on the wall, 96 bottles of beer.\nTake one down and pass it around, 95 bottles of beer on the wall.\n95 bottles of beer on the wall, 95 bottles of beer.\nTake one down and pass it around, 94 bottles of beer on the wall.\n94 bottles of beer on the wall, 94 bottles of beer.\nTake one down and pass it around, 93 bottles of beer on the wall.\n93 bottles of beer on the wall, 93 bottles of beer.\nTake one down and pass it around, 92 bottles of beer on the wall.\n92 bottles of beer on the wall, 92 bottles of beer.\nTake one down and pass it around, 91 bottles of beer on the wall.\n91 bottles of beer on the wall, 91 bottles of beer.\nTake one down and pass it around, 90 bottles of beer on the wall.\n90 bottles of beer on the wall, 90 bottles of beer.\nTake one down and pass it around, 89 bottles of beer on the wall.\n89 bottles of beer on the wall, 89 bottles of beer.\nTake one down and pass it around, 88 bottles of beer on the wall.\n88 bottles of beer on the wall, 88 bottles of beer.\nTake one down and pass it around, 87 bottles of beer on the wall.\n87 bottles of beer on the wall, 87 bottles of beer.\nTake one down and pass it around, 86 bottles of beer on the wall.\n86 bottles of beer on the wall, 86 bottles of beer.\nTake one down and pass it around, 85 bottles of beer on the wall.\n85 bottles of beer on the wall, 85 bottles of beer.\nTake one down and pass it around, 84 bottles of beer on the wall.\n84 bottles of beer on the wall, 84 bottles of beer.\nTake one down and pass it around, 83 bottles of beer on the wall.\n83 bottles of beer on the wall, 83 bottles of beer.\nTake one down and pass it around, 82 bottles of beer on the wall.\n82 bottles of beer on the wall, 82 bottles of beer.\nTake one down and pass it around, 81 bottles of beer on the wall.\n81 bottles of beer on the wall, 81 bottles of beer.\nTake one down and pass it around, 80 bottles of beer on the wall.\n80 bottles of beer on the wall, 80 bottles of beer.\nTake one down and pass it around, 79 bottles of beer on the wall.\n79 bottles of beer on the wall, 79 bottles of beer.\nTake one down and pass it around, 78 bottles of beer on the wall.\n78 bottles of beer on the wall, 78 bottles of beer.\nTake one down and pass it around, 77 bottles of beer on the wall.\n77 bottles of beer on the wall, 77 bottles of beer.\nTake one down and pass it around, 76 bottles of beer on the wall.\n76 bottles of beer on the wall, 76 bottles of beer.\nTake one down and pass it around, 75 bottles of beer on the wall.\n75 bottles of beer on the wall, 75 bottles of beer.\nTake one down and pass it around, 74 bottles of beer on the wall.\n74 bottles of beer on the wall, 74 bottles of beer.\nTake one down and pass it around, 73 bottles of beer on the wall.\n73 bottles of beer on the wall, 73 bottles of beer.\nTake one down and pass it around, 72 bottles of beer on the wall.\n72 bottles of beer on the wall, 72 bottles of beer.\nTake one down and pass it around, 71 bottles of beer on the wall.\n71 bottles of beer on the wall, 71 bottles of beer.\nTake one down and pass it around, 70 bottles of beer on the wall.\n70 bottles of beer on the wall, 70 bottles of beer.\nTake one down and pass it around, 69 bottles of beer on the wall.\n69 bottles of beer on the wall, 69 bottles of beer.\nTake one down and pass it around, 68 bottles of beer on the wall.\n68 bottles of beer on the wall, 68 bottles of beer.\nTake one down and pass it around, 67 bottles of beer on the wall.\n67 bottles of beer on the wall, 67 bottles of beer.\nTake one down and pass it around, 66 bottles of beer on the wall.\n66 bottles of beer on the wall, 66 bottles of beer.\nTake one down and pass it around, 65 bottles of beer on the wall.\n65 bottles of beer on the wall, 65 bottles of beer.\nTake one down and pass it around, 64 bottles of beer on the wall.\n64 bottles of beer on the wall, 64 bottles of beer.\nTake one down and pass it around, 63 bottles of beer on the wall.\n63 bottles of beer on the wall, 63 bottles of beer.\nTake one down and pass it around, 62 bottles of beer on the wall.\n62 bottles of beer on the wall, 62 bottles of beer.\nTake one down and pass it around, 61 bottles of beer on the wall.\n61 bottles of beer on the wall, 61 bottles of beer.\nTake one down and pass it around, 60 bottles of beer on the wall.\n60 bottles of beer on the wall, 60 bottles of beer.\nTake one down and pass it around, 59 bottles of beer on the wall.\n59 bottles of beer on the wall, 59 bottles of beer.\nTake one down and pass it around, 58 bottles of beer on the wall.\n58 bottles of beer on the wall, 58 bottles of beer.\nTake one down and pass it around, 57 bottles of beer on the wall.\n57 bottles of beer on the wall, 57 bottles of beer.\nTake one down and pass it around, 56 bottles of beer on the wall.\n56 bottles of beer on the wall, 56 bottles of beer.\nTake one down and pass it around, 55 bottles of beer on the wall.\n55 bottles of beer on the wall, 55 bottles of beer.\nTake one down and pass it around, 54 bottles of beer on the wall.\n54 bottles of beer on the wall, 54 bottles of beer.\nTake one down and pass it around, 53 bottles of beer on the wall.\n53 bottles of beer on the wall, 53 bottles of beer.\nTake one down and pass it around, 52 bottles of beer on the wall.\n52 bottles of beer on the wall, 52 bottles of beer.\nTake one down and pass it around, 51 bottles of beer on the wall.\n51 bottles of beer on the wall, 51 bottles of beer.\nTake one down and pass it around, 50 bottles of beer on the wall.\n50 bottles of beer on the wall, 50 bottles of beer.\nTake one down and pass it around, 49 bottles of beer on the wall.\n49 bottles of beer on the wall, 49 bottles of beer.\nTake one down and pass it around, 48 bottles of beer on the wall.\n48 bottles of beer on the wall, 48 bottles of beer.\nTake one down and pass it around, 47 bottles of beer on the wall.\n47 bottles of beer on the wall, 47 bottles of beer.\nTake one down and pass it around, 46 bottles of beer on the wall.\n46 bottles of beer on the wall, 46 bottles of beer.\nTake one down and pass it around, 45 bottles of beer on the wall.\n45 bottles of beer on the wall, 45 bottles of beer.\nTake one down and pass it around, 44 bottles of beer on the wall.\n44 bottles of beer on the wall, 44 bottles of beer.\nTake one down and pass it around, 43 bottles of beer on the wall.\n43 bottles of beer on the wall, 43 bottles of beer.\nTake one down and pass it around, 42 bottles of beer on the wall.\n42 bottles of beer on the wall, 42 bottles of beer.\nTake one down and pass it around, 41 bottles of beer on the wall.\n41 bottles of beer on the wall, 41 bottles of beer.\nTake one down and pass it around, 40 bottles of beer on the wall.\n40 bottles of beer on the wall, 40 bottles of beer.\nTake one down and pass it around, 39 bottles of beer on the wall.\n39 bottles of beer on the wall, 39 bottles of beer.\nTake one down and pass it around, 38 bottles of beer on the wall.\n38 bottles of beer on the wall, 38 bottles of beer.\nTake one down and pass it around, 37 bottles of beer on the wall.\n37 bottles of beer on the wall, 37 bottles of beer.\nTake one down and pass it around, 36 bottles of beer on the wall.\n36 bottles of beer on the wall, 36 bottles of beer.\nTake one down and pass it around, 35 bottles of beer on the wall.\n35 bottles of beer on the wall, 35 bottles of beer.\nTake one down and pass it around, 34 bottles of beer on the wall.\n34 bottles of beer on the wall, 34 bottles of beer.\nTake one down and pass it around, 33 bottles of beer on the wall.\n33 bottles of beer on the wall, 33 bottles of beer.\nTake one down and pass it around, 32 bottles of beer on the wall.\n32 bottles of beer on the wall, 32 bottles of beer.\nTake one down and pass it around, 31 bottles of beer on the wall.\n31 bottles of beer on the wall, 31 bottles of beer.\nTake one down and pass it around, 30 bottles of beer on the wall.\n30 bottles of beer on the wall, 30 bottles of beer.\nTake one down and pass it around, 29 bottles of beer on the wall.\n29 bottles of beer on the wall, 29 bottles of beer.\nTake one down and pass it around, 28 bottles of beer on the wall.\n28 bottles of beer on the wall, 28 bottles of beer.\nTake one down and pass it around, 27 bottles of beer on the wall.\n27 bottles of beer on the wall, 27 bottles of beer.\nTake one down and pass it around, 26 bottles of beer on the wall.\n26 bottles of beer on the wall, 26 bottles of beer.\nTake one down and pass it around, 25 bottles of beer on the wall.\n25 bottles of beer on the wall, 25 bottles of beer.\nTake one down and pass it around, 24 bottles of beer on the wall.\n24 bottles of beer on the wall, 24 bottles of beer.\nTake one down and pass it around, 23 bottles of beer on the wall.\n23 bottles of beer on the wall, 23 bottles of beer.\nTake one down and pass it around, 22 bottles of beer on the wall.\n22 bottles of beer on the wall, 22 bottles of beer.\nTake one down and pass it around, 21 bottles of beer on the wall.\n21 bottles of beer on the wall, 21 bottles of beer.\nTake one down and pass it around, 20 bottles of beer on the wall.\n20 bottles of beer on the wall, 20 bottles of beer.\nTake one down and pass it around, 19 bottles of beer on the wall.\n19 bottles of beer on the wall, 19 bottles of beer.\nTake one down and pass it around, 18 bottles of beer on the wall.\n18 bottles of beer on the wall, 18 bottles of beer.\nTake one down and pass it around, 17 bottles of beer on the wall.\n17 bottles of beer on the wall, 17 bottles of beer.\nTake one down and pass it around, 16 bottles of beer on the wall.\n16 bottles of beer on the wall, 16 bottles of beer.\nTake one down and pass it around, 15 bottles of beer on the wall.\n15 bottles of beer on the wall, 15 bottles of beer.\nTake one down and pass it around, 14 bottles of beer on the wall.\n14 bottles of beer on the wall, 14 bottles of beer.\nTake one down and pass it around, 13 bottles of beer on the wall.\n13 bottles of beer on the wall, 13 bottles of beer.\nTake one down and pass it around, 12 bottles of beer on the wall.\n12 bottles of beer on the wall, 12 bottles of beer.\nTake one down and pass it around, 11 bottles of beer on the wall.\n11 bottles of beer on the wall, 11 bottles of beer.\nTake one down and pass it around, 10 bottles of beer on the wall.\n10 bottles of beer on the wall, 10 bottles of beer.\nTake one down and pass it around, 9 bottles of beer on the wall.\n9 bottles of beer on the wall, 9 bottles of beer.\nTake one down and pass it around, 8 bottles of beer on the wall.\n8 bottles of beer on the wall, 8 bottles of beer.\nTake one down and pass it around, 7 bottles of beer on the wall.\n7 bottles of beer on the wall, 7 bottles of beer.\nTake one down and pass it around, 6 bottles of beer on the wall.\n6 bottles of beer on the wall, 6 bottles of beer.\nTake one down and pass it around, 5 bottles of beer on the wall.\n5 bottles of beer on the wall, 5 bottles of beer.\nTake one down and pass it around, 4 bottles of beer on the wall.\n4 bottles of beer on the wall, 4 bottles of beer.\nTake one down and pass it around, 3 bottles of beer on the wall.\n3 bottles of beer on the wall, 3 bottles of beer.\nTake one down and pass it around, 2 bottles of beer on the wall.\n2 bottles of beer on the wall, 2 bottles of beer.\nTake one down and pass it around, 1 bottle of beer on the wall.\n1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall."
  else NA 
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Expand a string
# Write a function expand() that takes a character vector of length 1 (a single string), and turns it into a character vector of all the characters in that string. If there are no characters in the string (see the second example), return an empty character vector (a character vector of length 0). Important note: make sure your function returns a character vector, not a list

expand <- function(s){
  vec <- vector("character", 0)
  if(nchar(s) == 0) vec
  else unlist(strsplit(s, ""))
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# All level 8 katas completed as of 4/10/23


