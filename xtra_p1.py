"""
Beth Harvey
January 14, 2023

Bonus task for Data Analytics Fundamentals Project 1:
The purpose of this module is to create a gamebot to play an interactive game with the
user. The skills used in this task include: input(), f-strings, and logic statements.

"""

import random

# Change the name below to a name of your choice

name = "BethsBot"

# Fix the code below to print the name using an f-string

print()
print(f"Hello, I'm {name}, your gamebot.")
print("Let's play an animal guessing game!")
print("There are 3 animals: wolf, eagle, snake (a Python of course).")
print("The wolf scares the eagle.")
print("The eagle grabs the snake.")
print("The snake bites the wolf.")
print("I'll pick one and you pick one and we'll see who wins.")
print()

# Right now, the user choses wolf everytime.
# Modify the code so the user is asked to
# enter wolf, eagle, or snake.
# Hint: use the input() function

user_choice = input('Enter wolf, eagle, or snake: ')

# Now the bot will pick one
buddy_choice = random.choice(["wolf", "eagle", "snake"])

# Report the choices
print()
print(f"You said {user_choice}.")
print(f"I said {buddy_choice}.")
print()


# Now we need to compare the choices and determine the winner
# Complete the logic to
# compare the choices and print who won
# In Python, indentation is important!
if user_choice == buddy_choice:
    print("We tied!")

if user_choice == 'wolf':
    if buddy_choice == 'eagle':
        print('Your wolf scares my eagle. You win!')
    if buddy_choice == 'snake':
        print('My snake bites your wolf. I win!!')

if user_choice == 'eagle':
    if buddy_choice == 'wolf':
        print('My wolf scares your eagle. I win!')
    if buddy_choice == 'snake':
        print('Your eagle grabs my snake. You win!')

if user_choice == 'snake':
    if buddy_choice == 'wolf':
        print('Your snake bites my wolf. You win!')
    if buddy_choice == 'eagle':
        print('My eagle grabs your snake. I win!')


# When you finish,
# right-click on the code and select "Format Document"

# Run the code, and play the game a few times.
# Copy the output from the terminal and paste it into the
# docstring comment below.
# --------------------------------------------------------------------
"""
/usr/bin/python3 "/Users/macbeth/Documents/Data Fundamentals/datafun-01-getting-started/xtra_p1.py"
(base) macbeth@beths-air datafun-01-getting-started % /usr/bin/python3 "/Users/macbeth/Documents/D
ata Fundamentals/datafun-01-getting-started/xtra_p1.py"

Hello, I'm BethsBot, your gamebot.
Let's play an animal guessing game!
There are 3 animals: wolf, eagle, snake (a Python of course).
The wolf scares the eagle.
The eagle grabs the snake.
The snake bites the wolf.
I'll pick one and you pick one and we'll see who wins.

Enter wolf, eagle, or snake: wolf

You said wolf.
I said eagle.

Your wolf scares my eagle. You win!
(base) macbeth@beths-air datafun-01-getting-started % /usr/bin/python3 "/Users/macbeth/Documents/D
ata Fundamentals/datafun-01-getting-started/xtra_p1.py"

Hello, I'm BethsBot, your gamebot.
Let's play an animal guessing game!
There are 3 animals: wolf, eagle, snake (a Python of course).
The wolf scares the eagle.
The eagle grabs the snake.
The snake bites the wolf.
I'll pick one and you pick one and we'll see who wins.

Enter wolf, eagle, or snake: eagle

You said eagle.
I said eagle.

We tied!
(base) macbeth@beths-air datafun-01-getting-started % /usr/bin/python3 "/Users/macbeth/Documents/D
ata Fundamentals/datafun-01-getting-started/xtra_p1.py"

Hello, I'm BethsBot, your gamebot.
Let's play an animal guessing game!
There are 3 animals: wolf, eagle, snake (a Python of course).
The wolf scares the eagle.
The eagle grabs the snake.
The snake bites the wolf.
I'll pick one and you pick one and we'll see who wins.

Enter wolf, eagle, or snake: snake

You said snake.
I said eagle.

My eagle grabs your snake. I win!
(base) macbeth@beths-air datafun-01-getting-started % /usr/bin/python3 "/Users/macbeth/Documents/D
ata Fundamentals/datafun-01-getting-started/xtra_p1.py"

Hello, I'm BethsBot, your gamebot.
Let's play an animal guessing game!
There are 3 animals: wolf, eagle, snake (a Python of course).
The wolf scares the eagle.
The eagle grabs the snake.
The snake bites the wolf.
I'll pick one and you pick one and we'll see who wins.

Enter wolf, eagle, or snake: eagle

You said eagle.
I said wolf.

My wolf scares your eagle. I win!



"""
