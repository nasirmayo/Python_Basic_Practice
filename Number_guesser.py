import random

while True:
    top_of_range = input("Type a number: ")
    if top_of_range.isdigit():
        top_of_range = int(top_of_range)
        if top_of_range <= 0:
            print("Please enter greater than 0 number next time")
            continue
        else:
            break
    else:
        print("please enter the digit next time")
        continue

random_number = random.randint(0, top_of_range)
guesses = 0
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("please enter the digit number next time")
        continue
    if user_guess == random_number:
        print("you got it!")
        print("You guess it in", guesses, "number of guesses")
        break
    elif user_guess > random_number:
        print("You are above number")
    else:
        print("You are below number")





