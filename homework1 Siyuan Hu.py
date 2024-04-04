# PPHA 30537
# Spring 2024
# Homework 1

# YOUR CANVAS NAME HERE 
# Siyuan Hu
# YOUR CNET ID NAME HERE 
# siyuanh
# YOUR GITHUB USER NAME HERE 
# 618SiyuanHu

# Due date: Sunday April 10th before midnight
# Write your answers in the space between the questions, and commit/push only this file to your repo.

#############
# Part 1: Introductory Python (to be done without defining functions or classes)

# Question 1.1: Using a for loop, write code that takes in any list of objects, then prints out:
# "The value at position __ is __" for every element in the loop, where the first blank is the
# index location and the second blank the object at that index location.

for everyob in list:
    print("The value at position '{}' is '{}'". format(list.index(everyob),everyob))

# Question 1.2: A palindrome is a word or phrase that is the same both forwards and backwards. Write
# code that takes a variable of any string, then tests to see whether it qualifies as a palindrome.
# Make sure it counts the word "radar" and the phrase "A man, a plan, a canal, Panama!", while
# rejecting the word "Microsoft" and the phrase "This isn't a palindrome". Print the results of these
# four tests.
import string
check_list=("radar","A man, a plan, a canal, Panama!","Microsoft","This isn't a palindrome")
for everystr in check_list:
    punctuation = string.punctuation
    clean_str= everystr.lower().replace(" ","").replace(",", "")
    for char in punctuation:
        clean_str = clean_str.replace(char, '')
    if clean_str==clean_str[::-1]:
        print(everystr+" is a palindrom")
    else:
        print(everystr+" is not a palindrom")

# Question 1.3: The code below pauses to wait for user input, before assigning the user input to the
# variable. Beginning with the given code, check to see if the answer given is an available
# vegetable. If it is, print that the user can have the vegetable and end the bit of code.  If
# they input something unrecognized by our list, tell the user they made an invalid choice and make
# them pick again. Repeat until they pick a valid vegetable.
available_vegetables = ['carrot', 'kale', 'broccoli', 'pepper']
while True:
    choice=input('Please pick a vegetable I have available: ')
    if choice in available_vegetables:
        print("You can have the "+choice)
        break
    else:
        print("You made an unvalid choice. Please pick again")


# Question 1.4: Write a list comprehension that starts with any list of strings and returns a new
# list that contains each string in all lower-case letters, unless the modified string begins with
# the letter "a" or "b", in which case it should drop it from the result.
newlist=[]
for everystring in list:
    if not (everystring.lower().startswith("a") or everystring.lower().startswith("b")):
        newlist=newlist+[everystring.lower()]

# Question 1.5: Beginning with the two lists below, write a single dictionary comprehension that
# turns them into the following dictionary: {'IL':'Illinois', 'IN':'Indiana', 'MI':'Michigan', 'WI':'Wisconsin'}
short_names = ['IL', 'IN', 'MI', 'WI']
long_names  = ['Illinois', 'Indiana', 'Michigan', 'Wisconsin']
new_dictionary={}
for i in range (4):
   new_dictionary.update({short_names[i]:long_names[i]})

#############
# Part 2: Functions and classes (must be answered using functions\classes)

# Question 2.1: Write a function that takes two numbers as arguments, then
# sums them together. If the sum is greater than 10, return the string 
# "big", if it is equal to 10, return "just right", and if it is less than
# 10, return "small". Apply the function to each tuple of values in the 
# following list, with the end result being another list holding the strings 
# your function generates (e.g. ["big", "big", "small"]).

start_list = [(10, 0), (100, 6), (0, 0), (-15, -100), (5, 4)]
def addupto(list):
    end_list=[]
    for everyob in list:
        a=sum(everyob)
        if a>10:
            end_list=end_list+["big"]
        elif a==10:
            end_list=end_list+["just right"]
        else:
            end_list=end_list+["small"]
    return end_list
addupto(start_list)                    

# Question 2.2: The following code is fully-functional, but uses a global
# variable and a local variable. Re-write it to work the same, but using one
# argument and no global variable. Use no more than two lines of comments to
# explain why this new way is preferable to the old way.

a = 10
def my_func():
    b = 40
    return a + b
x = my_func()

def new_func(x):
    c=x+40
    return c

# The new function uses less variables so it's easier to understand.

# Question 2.3: Write a function that can generate a random password from
# upper-case and lower-case letters, numbers, and special characters 
# (!@#$%^&*). It should have an argument for password length, and should 
# check to make sure the length is between 8 and 16, or else print a 
# warning to the user and exit. Your function should also have a keyword 
# argument named "special_chars" that defaults to True.  If the function 
# is called with the keyword argument set to False instead, then the 
# random values chosen should not include special characters. Create a 
# second similar keyword argument for numbers. Use one of the two 
# libraries below in your solution:
#import random
#from numpy import random
import random
def generate_password(length, special_chars=True, include_numbers=True):
    if length < 8 or length > 16:
        print("Error! Password length must be between 8 and 16.")
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    if include_numbers:
        chars = chars + '0123456789'
    if special_chars:
        chars = chars + '!@#$%^&*'
    password = ''.join(random.choice(chars) for _ in range(length))
    return password
# Question 2.4: Create a class named MovieDatabase that takes one argument
# when an instance is created which stores the name of the person creating
# the database (in this case, you) as an attribute. Then give it two methods:
#
# The first, named add_movie, that requires three arguments when called: 
# one for the name of a movie, one for the genera of the movie (e.g. comedy, 
# drama), and one for the rating you personally give the movie on a scale 
# from 0 (worst) to 5 (best). Store those the details of the movie in the 
# instance.
#
# The second, named what_to_watch, which randomly picks one movie in the
# instance of the database. Tell the user what to watch tonight,
# courtesy of the name of the name you put in as the creator, using a
# print statement that gives all of the info stored about that movie.
# Make sure it does not crash if called before any movies are in the
# database.
#
# Finally, create one instance of your new class, and add four movies to
# it. Call your what_to_watch method once at the end.
class MovieDatabase():
    def __init__(self,name_of_the_creator):
        self.name_of_the_creator=name_of_the_creator
        self.movielist=[]
    def add_movie(self,name,genera,rating):
        self.movielist=self.movielist+[(name,genera,rating)]
    def what_to_watch(self):
        if self.movielist==[]:
            print("No movies in the database.")
        else:
            watch_tonight=random.choice(self.movielist)
            print("Name:" + watch_tonight["name"]+
                  "Genera" + watch_tonight["genera"]+
                  "Rating" + watch_tonight["rating"])
new_moviedatabase=MovieDatabase("Siyuan")
new_moviedatabase.add_movie("Dune", "Science Fiction", 5)
new_moviedatabase.add_movie("The Godfather", "Crime", 5)
new_moviedatabase.add_movie("Scent of a Woman", "Drama", 5)
new_moviedatabase.add_movie("Dead Poets Society", "Drama", 5)
