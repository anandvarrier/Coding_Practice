"""
Task
-----
1) Build a Number guessing game, in which the user selects a range.
2) Let’s say User selected a range, i.e., from A to B, where A and B belong to Integer.
3) Some random integer will be selected by the system and the user has to guess that integer in the minimum number of guesses
"""
#Break down the porblem
"""
1) accept lower and upper bound from user and store the random number between that range
2) calculate the maximum number of guesses and store in a variable
3) accept number from user
4) check if the number is correct or not and also tell the number of guesses the user made
5) if not then tell the user that the guessed number is small or big
6) if the guessd number exceeds the max. of guessed number then give the actual answer
"""

import math
import random

lower = int(input("Enter the lower number of range:"))
upper = int(input("Enter the higher number of range:"))

r_num = random.randint(lower,upper)
max_no_guess = round(math.log(upper -lower + 1,2))

count = 0

while count < max_no_guess:
    count+=1

    guess = int(input("Guess the number:"))

    if guess == r_num:
        print("You have gussed the number right in {} guesses!".format(count))
        break 
    elif guess > r_num:
        print("Too high!")
    elif guess < r_num:
        print("Too low!")

if count >= max_no_guess:
    print("The correct answer is:{}".format(r_num))


"""
Time Complexity = O(n) because, the number of iterations is not fixed and depends upon the number of guesses
Space Complexity = O(1) because, all the variables are of the same time and no extra spcae is required.
"""
