print("Welcome to my game")

want_to_play = input("Do you want play? ")
if want_to_play.lower() != "yes":
    quit()
print("Okay! let's play")

score = 0
answer = input("What does CPU stand For? ").lower()
if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand For? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("What does RAM stand For? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("What does PSU stand For? ")
if answer.lower() == "power suply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")


