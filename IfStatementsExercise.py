
'''if temprature > 30:
    print("it's a hot day")
    print("drink plenty of water")
elif temprature > 20: # (20, 30]
    print("it's a nice day")
elif temprature > 10: # (10, 20]
    print("it's a bit cold")
else:
    print("It's cold out there")
print("Done")'''
'''
print("i am nasir", end=" ")
print("i live in lahore", end=" ")


while True:
    temprature = input("Type your city current Temprature or type q to Quit: ").lower()
    if temprature == "q":
        break
    if temprature.isdigit():
        print(type(temprature))
        if int(temprature) > 30:
            print("its a hot. drink plenty of water")
        elif int(temprature) > 20: #(20, 30]
            print("its little bit cold out there")
        elif int(temprature) > 10: #(10, 20]
            print("it's cold out ther")
        else: #(0 , 10]
            print("it's very cold out there")
    else:
        print("Please type digit number")
        continue

print("Goodbye!")
'''

print('--------------Shot hand if else---------------------')
a = 5
b  = 6

if b > a: print('b is greater than a')

print("A") if a > b else print("B")

print("A") if a > b else print("B") if a == b else print("C")

if a < b: c = 4
print(c)

