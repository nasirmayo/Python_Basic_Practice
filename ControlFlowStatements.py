# sequence statements

'''a = 10
b = 5
print("sum: ", a+b)
'''


# Selection statements:

# check which is bigger

'''a = 5
b = 10
c = 15
if a > b:
    if a > c:
        print("a is bigger")
    else:
        print("c is bigger")
elif b > c:
    print("b is bigger")
else:
    print("c is bigger")
'''

# a person is eligible for voting or not

'''user_age = int(input("Enter your Age:" ))
if user_age >=18:
    print("You are eligible for voting")
else:
    print("you are not eligible for voting")
'''


# number is even or not

'''number = int(input("Enter a number: "))
if number % 2 == 0:
    print("You enter a even number")
else:
    print("you enter a odd number")
'''

# check number is divisible by 7 or not

'''number = int(input("Enter a No: "))
if number % 7 == 0:
    print("number is divisible by 7")
else:
    print("number is not divisible by 7")
'''

# check if number multiple of 5 or not

'''num = int(input("Enter a No: "))
if num % 5 == 0:
    print("Hello")
else:
    print("Bye")
'''

# Calculate user electricity bill amount:

'''bill_ammount = 0
number_units = int(input("Enter your electricity units: "))
if number_units <= 100:
    bill_ammount = 0;
elif number_units <= 200: #(100, 200]
    bill_ammount = (number_units - 100) * 5
else:
    bill_ammount = 500 + (number_units - 200) * 10
print("Amount to pay ", bill_ammount,".")
'''

# display the last digit of any number. Note: %10 of any number show last digit

'''number = int(input("Enter the No: "))

print("Last digit of entered number is: ",number%10)
'''

#check if last digit of number is divisible by 3.

'''number = int(input("Enter the No: "))
if (number%10) % 3 == 0:
    print("last is divisible by 3")
else:
    print("not divisible by 3")
'''
# display the grades of students

'''student_percentage = int(input("Enter you Grades: "))
if student_percentage <= 100:
    if student_percentage < 60:
        print("you Grade is: ", "D")
    elif student_percentage <= 80:
        print("You Grade is: ", "C")
    elif student_percentage <= 90:
        print("You Grade is: ", "B")
    else:
        print("Your Grade is: ", "A")
else:
    print("Please enter percentage less than 100")
'''

# calculate the Road Tax of bike according to price.
'''tax_to_be_paid = 0;
bike_price = int (input("Enter the price of bike: "))
if bike_price > 1000000:
    tax_to_be_paid = (bike_price * 15) / 100
elif bike_price > 50000:
    tax_to_be_paid = (bike_price * 10) / 100
else:
    tax_to_be_paid = (bike_price * 5) / 100

print("Payable Tax is: ", tax_to_be_paid)
'''

# check whether an year is leap year or not

'''year = int (input("Enter the year"))

if year % 100 == 0:
    if year % 400 == 0:
        print("This Year is Leap year")
    else:
        print("This year is not leap year")
else:
    if year % 4 == 0:
        print("This year is leap year")
'''

# Accept number and display day with to number.

'''list = ('sunday', 'monday', 'tuesday','wednesday', 'thursday', 'friday', 'saturday')
number = int (input("Enter an number between 1 - 7: "))
print('Name of the Day: ', list[number - 1])
'''

# Accept number 1 -12 and display the month and days in that month again the number like 1 for january and day in january 31

'''month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
days_list = [31, 28, 30, 30, 30, 30, 31, 30, 30, 30, 30, 30]
number = int (input("Enter any number between 1 - 12: "))
print("Name of the Month is:", month_list[number - 1],"," ,"Number of day in this month are:", days_list[number - 1])
'''

# Accept city name and display monument of that city

'''city_name = input("Enter the name of city: ").lower()
if city_name == "delhi":
    print("The monument of Delhi is: " + "Red Fort")
elif city_name == "agra":
    print("The monument of Agra is: " + "Taj Mahal")
else:
    print("The monument of Jaipur: " + "Jal Mahal")
'''

''''a = 9
if a > 5 and a < 10:
    print("Hello")
else:
    print("Bye!")
'''

# find the if entered number is 3 digit or not

'''number = input("Enter any number: ")
print("Middle digit is: ", (int(number) % 100) // 10)
if len(number) == 3:
    print("number is 3 digit")
else:
    print("number is not 3 digit")
'''

# find if a person is senior citizen or not
'''age = int(input("Enter your age: "))
if age >= 60:
    print("You are a senior citizen")
else:
    print("Not a senior citizen")
'''

# find the lowest number from 2 numbers accepted from user
'''number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))
lowest_number = 0;
if number_1 > number_2:
    lowest_number = number_2
else:
    lowest_number = number_1
print("Lowest number is: ",lowest_number)
'''

# check number is accepted from user is positive or negative

'''number = int(input("Enter the number: "))
if number < 0:
    print("Number is negative")
else:
    print('number is positive')
'''

# check whether is number a even or odd

'''number = int(input("Enter a number: "))
if number % 2 == 0:
    print("number is even")
else:
    print("number is odd")
'''

# check whether a number is divisible by 2 and 3 both

'''number = int(input("Enter a number: "))
if number % 2 == 0 and number % 3 == 0:
    print("this number is divisible by both 2 and 3")
else:
    print("not divisible")
'''

# Q6. Accept the age of 4 people and display the youngest one?

'''p_age_1 = int(input("Enter person 1 age: "))
p_age_2 = int(input("Enter person 2 age: "))
p_age_3 = int(input("Enter person 3 age: "))
p_age_4 = int(input("Enter person 4 age: "))

if p_age_1 < p_age_2 and p_age_1 < p_age_3 and p_age_1 < p_age_4:
    print("person 1 is youngest one")
elif p_age_2 < p_age_1 and p_age_2 < p_age_3 and p_age_2 < p_age_4:
    print("person 2 is youngest one")
elif p_age_3 < p_age_1 and p_age_3 < p_age_2 and p_age_3 < p_age_4:
    print("peron 3 is youngest one")
else:
    print("person 4 is youngest one")
'''


# check whether water is boiling or not, get temprature from user

'''temprature = int(input("Enter the Temprature: "))
if temprature >= 100:
    print("the water is boiling")
else:
    print("water is not boiling")
'''

# check whether number is prime number or not which took from user
'''k = 0
number = int(input("Enter the Number: "))
if number == 0 or number == 1:
    k = 1

for i in range(2, number):
    if number % i == 0:
        k = 1
if k == 1:
    print("number is not prime")
else:
    print("number is prime")

'''

# check whether char is vowel or not

'''ch = input("Enter the character: ")
vowel = "aeiouAEIOU"
if ch in vowel:
    print("yes")
else:
    print("No")

'''

# Q1. Accept the following from the user and calculate the percentage of class attended:

'''number_of_working_day = int(input("Enter Total number of working days: "))
days_of_absent  = int(input("Enter the total number of absentees: "))
attendance_perc = ((number_of_working_day - days_of_absent) / number_of_working_day) * 100
print("Attendance percntage: ", attendance_perc)
if attendance_perc < 75:
    print("Student is not permitted to sit in class")
'''

# Q3. A company decided to give bonus to employee according to following criteria: Time period of Service                Bonus
#
#     More than 10 years             10%
#
#     >=6 and <=10                   8%
#
#     Less than 6 years              5%
# Ask user for their salary and years of service and print the net bonus amount.

'''current_salary = float(input("Enter your current salary: "))
years_of_service  = float(input("Enter your years of service for company: "))
if years_of_service > 10:
    print("your Bunus is: ",(10/100) * current_salary)
elif years_of_service >=6 and years_of_service <= 10:
    print("your Bunus is: ",(8/100) * current_salary)
else:
    print("your Bunus is: ",(5/100) * current_salary)

'''

# Q4. Accept the marked price from the user and  calculate the Net amount as(Marked Price –    Discount) to pay according to following criteria:

'''marked_price = int(input("Enter the marked price: "))
net_amount = 0;
if marked_price > 10000:
    net_amount = marked_price - (20/100) * marked_price
elif marked_price > 7000: #(70000, 10000]
    net_amount = marked_price - (15/100) * marked_price
else:
    net_amount = marked_price - (10/100) * marked_price

print("Net amount neet to pay: ",net_amount)

'''

# Q5. Write a program to accept percentage and display the Category according to the  following criteria :
'''percentage = int(input("Enter the percenage: "))
if percentage < 40:
    print("Catagory: ","Fail")
elif percentage < 55:
    print("Catagory: ","Fair")
elif percentage < 65:
    print("Catagory: ","Good")
else:
    print("Catagory: ","Excellent")
'''
# Q6. Accept three sides of a triangle and check whether it is an equilateral, isosceles or scalene triangle.

'''tri_side_1 = int(input("Enter Side 1: "))
tri_side_2 = int(input("Enter side 2: "))
tri_side_3 = int(input("Enter side 3: "))
if tri_side_1 == tri_side_2 == tri_side_3:
    print("it's a triangle")
elif tri_side_1 == tri_side_2 or tri_side_2 == tri_side_3 or tri_side_1 == tri_side_3:
    print("It's isosceles")
else:
    print("it's a scalene")
'''
# Q7. Write a program to accept two numbers and mathematical operators and perform operation accordingly.

'''number_1 = float(input("Enter the first number: "))
number_2 = float(input("Enter the second number: "))
operator = input("Enter the Operator(+,-,*,/): ")
if operator == "+":
    print("Result: ",number_1+number_2)
elif operator == "-":
    print("Result: ",number_1-number_2)
elif operator == "*":
    print("Result: ",number_1*number_2)
else:
    print("Result: ",number_1/number_2)
'''

# Q8. Accept the age, sex (‘M’, ‘F’), number of days and display the wages accordingly

'''age = int(input("Enter the age: "))
gender = input("Enter the Gender: ").lower()
if age >= 18 and age < 30:
    if gender == "m":
        print("Wages are: ", 700)
    else:
        print("wage are: ", 750)
elif age >= 30 and age <= 40:
    if gender == "m":
        print("Wages are: ", 800)
    else:
        print("Wages are: ", 850)
else:
    print("please enter the age between (18,40)")
'''
# Q1. Accept three numbers from the user and display the second largest number.

number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))
number_3 = int(input("Enter the third number: "))
if (number_1 > number_2 and number_1 < number_3) or (number_1 < number_2 and number_1 > number_3):
    print("first is second largest")
elif (number_2 > number_1 and number_2 < number_3) or (number_2 < number_1 and number_2 > number_3):
    print("second is second largest")
else:
    print("thirsd number is second largest")