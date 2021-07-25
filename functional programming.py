#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']
#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]
#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]
#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

#map function
def capital(item):
    return item.upper()
print(list(map(capital,my_pets)))

#zip function
my_numbers.sort()
print(list(zip(my_strings,my_numbers)))

#filter function
def scorefilter(item):
    return item>50
print(list(filter(scorefilter,scores)))

#reduce function
from functools import *
def accumlator(acc,item):
    return acc + item
print(reduce(accumlator,(my_numbers + scores)))
