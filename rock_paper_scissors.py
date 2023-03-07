import random

user_wins = 0
Computer_wins = 0

rock_paper_scissor = ["rock", "paper", "scissor"]

while True:
    user_input = input("Type Rock/Paper/Scissor or type Q for Quit! ").lower()
    if user_input == "q":
        break
    if user_input not in rock_paper_scissor:
        continue

    random_number = random.randint(0, 2)
    computer_pick = rock_paper_scissor[random_number]
    print("Computer Picked:", computer_pick)
    if user_input == "rock" and computer_pick == "scissor":
        print("You Won!")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You Won!")
        user_wins += 1
    elif user_input == "scissor" and computer_pick == "paper":
        print("You Won!")
        user_wins += 1
    else:
        print("Computer Won!")
        Computer_wins += 1


print("You Won", user_wins, "times.")
print("Computer Won", Computer_wins, "times")
print("Goodbye!")


