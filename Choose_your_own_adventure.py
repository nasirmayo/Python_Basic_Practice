name = input("Type you name: ").lower()
print("Welcome", name, "to this adventure game")

answer = input(
    "you are on a dirt road, it has come to end and you need to go left or right, type left to go left or type right to go right: " ).lower()
if answer == "left":
    left_Q1 = input("You come to a river, you can walk or swim. Type walk to walk around or Type Swim to Swim ").lower()
    if left_Q1 == "swim":
        print("You swam across and eaten by aligator.")
    elif left_Q1 == "walk":
        print("you walked many miles and run out of water and loose the game")
    else:
        print("Note a valid option. you lose")
elif answer == "right":
    right_Q1 = input("You come to a bridge, it look wobbly, do you want to cross it or want to go back (cross/back)? ").lower()
    if right_Q1 == "back":
        print("You go back and lose")
    elif right_Q1 == "cross":
        right_Q2 = input("You cross the bridge and talk to a strangers. Do you talk to them (yes/no)? ").lower()
        if right_Q2 == "yes":
            print("you talk to strangers and they gave you gold and you won!")
        elif right_Q2 == "no":
            print("you ignore the strangers and they offended and you lose!")
        else:
            print("Note a valid option. you lose")

else:
    print("Note a valid option. you lose")


print("thankyou for trying" , name)