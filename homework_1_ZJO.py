# PPHA 30535
# Spring 2021
# Homework 1

# Zachary Obstfeld
# ZacharyObstfeld

# Due date: Sunday April 11th before midnight
# Write your answers in the space between the questions, and commit/push only this file to your repo.
# Note that there can be a difference between giving a "minimally" right answer, and a really good
# answer, so it can pay to put thought into your work.

#############

# Question 1: Using a for loop, write code that takes in any list of objects, then prints out:
# "The value at position __ is __" for every element in the loop, where the first blank is the
# index location and the second blank the object at that index location.

my_list = ['a', 'b', 'C']
index = 0
for item in my_list:
    print('The value at position ' + str(index) + ' is ' + str(item))
    index += 1
    

# Question 2: A palindrome is a word or phrase that is the same both forwards and backwards. Write
# code that takes a variable of any string, then tests to see whether it qualifies as a palindrome.
# Make sure it counts the word "radar" and the phrase "A man, a plan, a canal, Panama!", while
# rejecting the word "Apple" and the phrase "This isn't a palindrome". Print the results.

my_string = 'Hanna'
my_string = 'Hannah'
palindrome = my_string.lower()[::-1]
if palindrome == my_string.lower():
    print('This is a palindrome')
else:
    print("This isn't a palindrome")


# Question 3: The code below pauses to wait for user input, before assigning the user input to the
# variable.  Beginning with the given code, check to see if the answer given is an available
# vegetable.  If it is, print that the user can have the vegetable and end the bit of code.  If
# they input something unrecognized by our list, tell the user they made an invalid choice and make
# them pick again.  Repeat until they pick a valid vegetable.
available_vegetables = ['carrot', 'kale', 'radish', 'pepper']
choice = input('Please pick a vegetable I have available: ')
while choice != 'carrot' or choice != 'kale' or choice != 'radish' or choice != 'pepper':
    if choice == 'carrot' or choice == 'kale' or choice == 'radish' or choice == 'pepper':
        print('nice veggie, you can have it')
        break
    else:
        print('You have made an invalid choice!')
        choice = input('Please pick a vegetable I have available: ')


# Question 4: Write a list comprehension that starts with any list of strings, and returns a new
# list that contains each string in all lower-case letters, but only if the string begins with the
# letter "a" or "b".

my_list = ['aH', 'B']
lower_and_conditional= [item.lower() for item in my_list if item[0] == 'a' or item[0] == 'b']
lower_and_conditional

# Question 5: Beginning with the list below, write a single list comprehension that turns it into
# the following list: [26, 22, 18, 14, 10, 6]

#Source: https://www.geeksforgeeks.org/python-double-each-list-element/
#learn difference between .reverse() method and reversed() function
start_list = [3, 5, 7, 9, 11, 13]
rlist = [item * 2 for item in reversed(start_list)]

# Question 6: Beginning with the two lists below, write a single dictionary comprehension that
# turns them into the following dictionary: {'IL':'Illinois', 'IN':'Indiana', 'MI':'Michigan', 'OH':'Ohio'}

# Source: https://www.geeksforgeeks.org/python-dictionary-comprehension/
short_names = ['IL', 'IN', 'MI', 'OH']
long_names  = ['Illinois', 'Indiana', 'Michigan', 'Ohio']
new_dict = { k:v for (k,v) in zip(short_names, long_names)}  
