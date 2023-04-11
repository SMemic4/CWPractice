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

# Codewar Practice - Level 7 Katas

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# No oddities here
# Write a small function that returns the values of an array that are not odd. All values in the array will be integers. Return the good values in the order they are given.

no_odds <- function(values){
  vec1 <- which(values %% 2 == 0) # Holds the indices that will be referred  to later 
  vec2 <- vector("numeric", length(vec1)) # The vector that will hold the values
  for(i in seq_along(vec2))
  {
    n <- vec1[i] # Placeholder number to extract values
    vec2[i] <- values[n] 
  }
  vec2
}

# Shorter alternative

no_odds <- function(values){
  values<- values[values %% 2 == 0]
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Descending Order
# Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

descending_order <- function(num){
  as.double(paste(sort(as.double(unlist(strsplit(as.character(num), ""))), decreasing = TRUE), collapse = ""))
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Write a function that takes a positive integer n, sums all the cubed values from 1 to n (inclusive), and returns that sum.
# Assume that the input n will always be a positive integer.

sum_cubes <- function(n){
  sum(seq(1,n)^3)
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# A square of squares
# Given an integral number, determine if it's a square number:

is_square <- function(n){
  x <- 2*n - 2*(n-1)
  y <- 2*n-1
  ifelse(near(x,y), TRUE, FALSE)
}
is_square(25)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Sum of angles
# Find the total sum of internal angles (in degrees) in an n-sided simple polygon. N will be greater than 2.

angle <- function(n) {
  (n-2)*180
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Beginner Series #3 Sum of Numbers
# Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.

get_sum <- function(a, b){
  ifelse(a == b, a, sum(seq(a,b)))
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Shortest Word
# Simple, given a string of words, return the length of the shortest word(s). String will never be empty and you do not need to account for different data types.

find_short <- function(s){
  min(nchar(unlist(strsplit(s, " "))))
}
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Complementary DNA
# Your function receives one side of the DNA (string, except for Haskell); you need to return the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).


ccc <- "ATTGC"
ccc2 <- unlist(strsplit(ccc, ""))

lapply(X = ccc2, gsub("A", "T", gsub("T", "A", gsub("G", "C", gsub("C", "G", ccc2)))))


gsub("A", "T", gsub("T", "A", gsub("G", "C", gsub("C", "G", ccc2))))
