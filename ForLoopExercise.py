'''numbers = [1, 2, 3, 4, 5, 6, 7]

for items in numbers:
    print(items)
'''
import random
import re
import readline

# Exercise 1: Print First 10 natural numbers using while loop
'''i  = 1
while i <= 10:
    print(i)
    i += 1
'''
# Exercise 2: Print the following pattern
'''i = 5
for i in range(1, i + 1, 1):
    for j in range(1, i+1):
        print(j, end=" ")
    print("")
'''

# Exercise 3: Calculate the sum of all numbers from 1 to a given number

'''number = int(input("Enter the number: "))
i = 0
for j in range(1, number+1):
    i = i + j
print("sum is: ",i)
'''

# Exercise 4: Write a program to print multiplication table of a given number
'''number = int(input("Enter the number: "))
for j in range(1, 11):
    print(number,"x", j, " = ", number*j)
'''
# Exercise 5: Display numbers from a list using loop
'''numbers = [12, 75, 150, 180, 145, 525, 50]
for item in numbers:
    if item > 500:
        break
    elif item > 150:
        continue
    elif item % 5 == 0:
        print(item)
'''
# Exercise 6: Count the total number of digits in a number
'''number = 75869
count = 0
while number != 0:
    number = number // 10
    count += 1
print(count)
'''

# Exercise 7: Print the following pattern
'''k = 5
for i in  range(0, 6, 1):
    for j in range(k-i,0, -1):
        print(j, end=" ")
    print("")
'''
# Exercise 8: Print list in reverse order using a loop
'''for i in range(50, 0, -10):
    print(i)
'''
# Exercise 9: Display numbers from -10 to -1 using for loop
'''for i in range(-10, 0, 1):
    print(i)
'''
# Exercise 10: Use else block to display a message “Done” after successful execution of for loop
'''for i in range(5):
    print(i)
else:
    print("Done!")
'''
# Exercise 11: Write a program to display all prime numbers within a range
'''Start = 25
end = 50
for i in range(Start, end+1, 1):
    for j in range(2, i, 1):
        if i % j == 0:
            break
    else:
        print(i)

'''
# Exercise 12: Display Fibonacci series up to 10 terms

'''num_1 = 0
num_2 = 1
sum = 0
for i in range(100):
    print(num_1, end=" ")
    sum = num_1 + num_2
    num_1 = num_2
    num_2 = sum
'''

# Exercise 13: Find the factorial of a given number
'''number = int(input("Enter the number: "))
if number > 0:
    for i in range(number - 1, 0, -1):
        number = number * i

    print(number)
else:
    print("Please Enter positive number")
'''
# Exercise 14: Reverse a given integer number
'''number = int(input("Enter the number: "))
number2 = number
print("Given Number: ",number)

# first solution
reverse_number = 0;
while number > 0:
    remainder = number%10
    reverse_number = (reverse_number*10) + remainder
    number = number//10
print("Reverse number: ", reverse_number)

# second solution
revers_str= []
while number2 > 0:
    reminder = number2%10
    revers_str.append(reminder)
    number2 = number2//10

print("Reverse number: ", end="")
for item in revers_str:
    print(item, end="")

'''

# Exercise 15: Use a loop to display elements from a given list present at odd index positions

'''my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in range(0, len(my_list)):
    if i%2 != 0:
        print(my_list[i])
'''
# Exercise 16: Calculate the cube of all numbers from 1 to a given number
'''give_number = 6
for i in range(1, 7, 1):
    print("Current number is : ",i,"and the cube is :", i*i*i)
    
'''
# Exercise 17: Find the sum of the series upto n terms

'''n = 5
# first number of sequence
start = 2
sum_seq = 0

# run loop n times
for i in range(0, n):
    print(start, end="+")
    sum_seq += start
    # calculate the next term
    start = start * 10 + 2
print("\nSum of above series is:", sum_seq)
'''

'''list1 = [10, 20, 30, 40, 50]
for item in list1[::-1]:
    print(item)
'''
# Write a for loop so that every item in the list is printed.
'''lst=["koala", "cat", "fox", "panda", "chipmunk", "sloth", "penguin", "dolphin"]
for item in lst:
    print(item, end=" ")
'''
# Write a for loop which print "Hello!, " plus each name in the list. i.e.: "Hello!, Sam"

'''lst=["Sam", "Lisa", "Micha", "Dave", "Wyatt", "Emma", "Sage"]
for item in lst:
    print("Hello!",item)
'''
# Write a for loop that iterates through a string and prints every letter.

'''str = 'Antarctica'
for item in str:
    print(item, end=" ")
'''

# Using a for loop and .append() method append each item with a Dr. prefix to the lst.
'''lst1=["Phil", "Oz", "Seuss", "Dre"]
lst2 = []
for item in lst1:
    lst2.append(item)
    print("Dr.", item)
'''
# Write a for loop which appends the square of each number to the new list.
'''list1 = [1,3,4,5,6,7,8,9]
list2 = []
for item in list1:
    list2.append(item**3)
print(list2)
'''
# Write a for loop using an if statement, that appends each number to the new list if it's positive.
'''lst1=[111, 32, -9, -45, -17, 9, 85, -10]
lst2 = []
for item in lst1:
    if item >= 0:
        lst2.append(item)
print(lst2)
'''
# Using for loop and if statement, append the value minus 1000 for each key to the new list if the value is above 1000. i.e.: if the value is 1500, 500 should be added to the new list.
'''dict={"z1":900, "t1": 1100, "p1": 2300, "r1": 1050, "k1": 3200, "g1": 400}
lst = []
for item in dict:
    if dict[item] > 1000:
        lst.append(dict[item] - 1000)
print(lst)
'''

# Write a for loop which appends the type of each element in the first list to the second list.
'''lst1=[3.14, 66, "Teddy Bear", True, [], {}]
lst2 = []
for item in lst1:
    lst2.append(type(item))
print(lst2)
'''
# Exercise 1: Write a program in Python to display the Factorial of a number.
'''number = int(input("Enter the number: "))
factorial = 4
for item in range(number - 1, 1, -1):
    number = number * item
print(number)
'''
# Exercise 2: Write a program in Python to reverse a word.
'''word = 'python'
print(len(word))
for item in range(len(word) - 1, -1, -1):
    print(word[item], end="")
'''
# Exercise 3: Write a Python program to reverse a number.
'''number  = 1234567
print(len(str(number)))
for item in range(0, len(str(number))):
    print(number%10 ,end="")
    number = number // 10
'''
# Exercise 4: Write a program to print n natural number in descending order using a while loop.
'''number = int(input("Enter the number: "))
while number > 0:
    print(number, end=" ")
    number -= 1
'''
# Exercise 5: Write a program to display the first 7 multiples of 7.
'''number = 0
multiple_count = 0
while True:
    if number%7 == 0:
        print(number)
        multiple_count += 1
    if multiple_count == 7:
        break
    number += 1;
'''
# Exercise 6: Write a program that appends the square of each number to a new list.
'''lts1 = [2,3,4,5,6,7,8,9]
lst2 = []
for item in lts1:
    lst2.append(item**2)
print(lst2)
'''
# Exercise 7: WAP to separate positive and negative number from a list.
'''given_lst = [23,-4,20,15,50,-9,-8,-3,100]
negative_lst = []
positive_lst = []
for item in given_lst:
    if item > 0:
        positive_lst.append(item)
    else:
        negative_lst.append(item)
print(positive_lst)
print(negative_lst)
'''
# Exercise 9: Write a program to filter even and odd number from a list.
'''lst1 = [23,45,3,59,30,20,90,19,35]
even_lst = []
odd_lst = []
for item in lst1:
    if item%2 == 0:
        even_lst.append(item)
    else:
        odd_lst.append(item)
print(even_lst)
print(odd_lst)
'''
# Exercise 10: Write a program to fetch only even values from a dictionary.
'''dict = {'v1':4,'v2':50,'v3':13,'v4':21,'v5':31,'v6':30,'v7':54,'v8':99,'v9':91}
list = []
for item in dict:
    if dict[item]%2 == 0:
        list.append(dict[item])
print(list)
'''

# 1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
'''num = []
for x in range(1500, 2701):
    if x % 7 == 0 and x % 5 == 0:
        num.append(str(x))
print(','.join(num))'''


# 2. Write a Python program to convert temperatures to and from celsius, fahrenheit. Go to the editor
# [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]

'''temprature = input("Enter the temprature you want to convert? (e.g., 45F, 102C etc.): ")
degree = int(temprature[:-1])
print(degree)
i_convert = temprature[-1]
print(i_convert)
if i_convert.upper() == "C":
    result = int(round((9 * degree) / 5 + 32))
    o_convention = "Fahrenheit"
elif i_convert.upper() == "F":
    result = int(round((degree - 32) * 5 / 9))
    o_convention = "Celsius"

else:
    print("Input proper convention")

print("The temperature in", o_convention, "is", result, "degrees.")'''


# Write a Python program to guess a number between 1 to 9. Go to the editor
# Note : User is prompted to enter a guess.
# If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.

'''random_number, guess_number = random.randint(1,10), 0
while True:
    guess_number = input("Enter a number between 1 - 9 or press 'q' to quit: ").lower()
    if guess_number == 'q':
        break
    if guess_number.isdigit():
        if int(guess_number) == random_number:
            print("Well guessed!")
            break
        else:
            continue
    else:
        print("Please enter the digit number between 1 - 9")
        continue'''


'''4. Write a Python program to construct the following pattern, using a nested for loop.
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*


for x in range(1, 6):
    for y in range(x):
        print("*", end= " ")
    print()
for x in range(4, 0, -1):
    for y in range(x):
        print("*", end= " ")
    print()
'''

# 5. Write a Python program that accepts a word from the user and reverse it. Go to the editor
'''user_word = input("Enter a word: ")
lst_word = []
for x in range(len(user_word) - 1, -1, -1):
    print(user_word[x], end="")
'''

# 6. Write a Python program to count the number of even and odd numbers from a series of numbers. Go to the editor
'''even_count, odd_count = 0, 0
number = [1,2,3,4,5,6,7,8,9]
for x in number:
    if x % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Number of even numbers: ", even_count)
print("Number of odd numbers: ", odd_count)'''

# 7. Write a Python program that prints each item and its corresponding type from the following list.

'''datalist = [1452, 11.23, 1 + 2j, True, 'w3resource', (0, -1), [5, 12], {"class": 'V', "section": 'A'}]
for x in datalist:
    print(type(x))'''

# 8. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.

'''num_lst = [0,1,2,3,4,5,6]
for x in num_lst:
    if x != 3 and x != 6:
        print(x, end=" ")
        continue
print()'''

# 9. Write a Python program to get the Fibonacci series between 0 to 50. Go to the editor
'''faninaci_lst = []
prev_num1 = 0
prev_num2 = 1
for x in range(1, 51):
    if prev_num2 < 50:
        faninaci_lst.append(prev_num2)
        prev_num1, prev_num2 = prev_num2, prev_num1+prev_num2
    else:
        break

print(faninaci_lst)


x,y=0,1

while y<50:
    print(y)
    x,y = y,x+y'''

# 10. Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

'''for x in range(1, 51):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 5 == 0:
        print("Buzz")
    elif x % 3 == 0:
        print("Fizz")
    else:
        print(x)'''

# Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
# Note :
# i = 0,1.., m-1
# j = 0,1, n-1.

'''row_num = int(input("Input the number of Rows: "))
column_num = int(input("Input the number of columns: "))
multi_list = [[0 for col in range(column_num)] for row in range(row_num)]
print(multi_list)
for row in range(row_num):
    for col in range(column_num):
        multi_list[row][col] = row * col
print(multi_list)'''

# 12. Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output (all characters in lower case).
'''lines = []
while True:
    line = input('')
    if not line:
        break
    else:
        lines.append(line.upper())

print(lines)
for line in lines:
    print(line)'''

# 13. Write a Python program which accepts a sequence of comma separated 4 digit binary numbers as its input and print the numbers that are divisible by 5 in a comma separated sequence.
#Sample Data : 0100,0011,1010,1001,1100,1001
# Expected Output : 1010
'''item = []
num = [x for x in input().split(',')]
for p in num:
    x = int(p)
    if x % 5 == 0:
        item.append(x)

print(item)'''

# 14. Write a Python program that accepts a string and calculate the number of digits and letters.
# Sample Data : Python 3.2
# Expected Output :
# Letters 6
# Digits 2
'''d = l = 0
string = input()
for x in string:
    if x.isdigit():
        d += 1
    elif x.isalpha():
        l += 1
    else:
        pass
print(l)
print(d)'''


# Write a Python program to check the validity of a password (input from users).
# Validation :
#
#     At least 1 letter between [a-z] and 1 letter between [A-Z].
#     At least 1 number between [0-9].
#     At least 1 character from [$#@].
#     Minimum length 6 characters.
#     Maximum length 16 characters.
'''import re

password = input()
x = True
while x:
    if len(password) < 6 or len(password) > 16:
        break
    elif not re.search("[a-z]", password):
        break
    elif not re.search('[A-Z]', password):
        break
    elif not re.search('[0-9]', password):
        break
    elif not re.search('[$#@]', password):
        break
    elif re.search('\s', password):
        break
    else:
        print('password is valid')
        x = False
        break

if x:
    print('Password is not Valid')

'''

# 16. Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number.
# The numbers obtained should be printed in a comma-separated sequence.
'''num_lst = []
is_divisible = True
for x in range(100, 401):
    num = str(x)
    for y in num:
        if int(y) % 2 == 0:
            is_divisible = True
        else:
            is_divisible = False
            break
    if is_divisible:
        num_lst.append(str(x))

print(','.join(num_lst))'''

# Write a Python program to print alphabet pattern 'A'.

'''result_str=""
for row in range(0,7):
    for column in range(0,7):
        if (((column == 1 or column == 5) and row != 0) or ((row == 0 or row == 3) and (column > 1 and column < 5))):
            result_str=result_str+"*"
        else:
            result_str=result_str+" "
    result_str=result_str+"\n"
print(result_str)'''

# 18. Write a Python program to print alphabet pattern 'D'.

'''result_str = ""
for row in range(0,7):
    for col in range(0,7):
        if ((row == 0 or row == 6) and (col > 0 and col < 5)) or ((col == 1 or col == 5) and (row != 0 and row != 6)):
            result_str = result_str+"*"
        else:
            result_str = result_str+" "
    result_str = result_str+'\n'

print(result_str)'''

# 19. Write a Python program to print alphabet pattern 'E'.
'''result_str = ''
for row in range(0,7):
    for col in range(0,7):
        if ((row == 0 or row == 6) and (col > 0 and col < 6)) or (row == 3 and (col > 0 and col < 5)) or (col == 1):
            result_str = result_str+"*"
        else:
            result_str = result_str+" "
    result_str = result_str+'\n'

print(result_str)'''

# 20. Write a Python program to print alphabet pattern 'G'.

'''result_str = ''
for row in range(0, 7):
    for col in range(0, 7):
        if ((row == 0 or row == 6) and (col > 1 and col < 5)) or ((row == 3) and ((col > 0 and col < 6) and (col != 2))) or ((col == 1 or col == 5) and ((row > 0 and row < 6) and row != 2)) or (row == 2 and col == 1):
            result_str = result_str+'*'
        else:
            result_str = result_str+' '
    result_str = result_str+'\n'
print(result_str)'''

# 21. Write a Python program to print alphabet pattern 'L'.
'''result_str = ''
for row in range(0, 7):
    for col in range(0, 7):
        if (row == 6 and col > 0 and col < 6) or (col == 1 and row < 6):
            result_str = result_str+'*'
        else:
            result_str = result_str+' '
    result_str = result_str+'\n'
print(result_str)'''

# 22. Write a Python program to print alphabet pattern 'M'.
'''result_str = ''
for row in range(0, 7):
    for col in range(0, 7):
        if (col == 1 or col == 5) or (row == 2 and col > 0 and col < 6 and col != 3) or (row == 3 and col == 3):
            result_str = result_str+'* '
        else:
            result_str = result_str+'  '
    result_str = result_str+'\n'
print(result_str)'''

# 26. Write a Python program to print the following patterns.
'''result_str = ''
for row in range(0, 15):
    for col in range(0, 17):
        if (row < 3 and col < 17) or (row > 5 and row < 9 and col < 17) or (row > 2 and row < 6 and col < 4) or (row > 8 and row < 12 and col > 12) or (row > 11 and col < 17):
            print('0', end='')
        else:
            print(' ', end='')
    result_str = result_str+'\n'
    print('')
#print(result_str)'''

# Write a Python program to calculate a dog's age in dog's years.
#  Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.
'''h_age = int(input("Enter the dog age in human years: "))
if h_age < 0:
    print("Enter positive number!")
    exit()
elif h_age <=2:
    dog_age = h_age * 10.5
else:
    dog_age = 21 + (h_age - 2)*4

print(dog_age)'''

# 32. Write a Python program to check whether an alphabet is a vowel or consonant. Go to the editor
#letter_aphabet = input("Enter the alphabet letter: ").lower()
'''if not re.search('[aeoiu]', letter_aphabet):
    print(letter_aphabet + " is not vowal")
else:
    print(letter_aphabet + ' is vowal')'''
'''vowal_lst = 'aeiouy'
if letter_aphabet in vowal_lst:
    if letter_aphabet == 'y':
        print(letter_aphabet + ' is some time vowal and some time not vowal')
    else:
        print(letter_aphabet + ' is vowal')
else:
    print(letter_aphabet + " is not vowal")'''

# 33. Write a Python program to convert month name to a number of days.

'''month_dict = {'january': 31, "febrary": '29/28', 'march': 31, 'april': 30, 'may': 31, 'june': 30, 'july': 31, 'august': 31, 'september': 30, 'october': 31, 'november': 30, 'december': 31}
month_name = input("Enter the month name: ").lower()
print(month_name+ " have " + str(month_dict[month_name]) + " days")'''

# 34. Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.

'''def sum (x , y):
    if x+y in range(15,20):
        return 20
    else:
        return x+y

print(sum(10,5))
print(sum(20,5))
print(sum(15, 5))'''

# 35. Write a Python program to check a string represent an integer or not.
'''def check_stirng(_string):
    if _string.isalpha():
        return "it is alphbetical"
    elif _string.isalnum():
        return 'it is Alpha numerc'
    else:
        return 'yes it is iteger'

print(check_stirng('hello'))
print(check_stirng("123412nds"))
print(check_stirng("1234"))'''

# 36. Write a Python program to check a triangle is equilateral, isosceles or scalene.
'''print("Input lengths of the triangle sides: ")
side_1 = int(input("x: "))
side_2 = int(input("y: "))
side_3 = int(input("z: "))
if side_1 == side_2 == side_3:
    print("Triangle is a equilatral")
elif side_1 != side_2 != side_3:
    print("Triangle is a scalene")
else:
    print("Triangle is a isosceles")
'''

# 37. Write a Python program that reads two integers representing a month and day and prints the season for that month and day.
'''month_name = input("Enter month (e.g. January, February etc.): ").lower()
num_days_in_month = int(input("Enter the number of days: "))
if month_name.title() in ('January', 'February', 'March'):
    season = 'winter'
elif month_name.title() in ('April', 'May', 'June'):
    season = 'spring'
elif month_name.title() in ('July', 'August', 'September'):
    season = 'summer'
else:
    season = 'autumn'


if (month_name.title() == 'March') and (num_days_in_month > 19):
	season = 'spring'
elif (month_name.title() == 'June') and (num_days_in_month > 20):
	season = 'summer'
elif (month_name.title() == 'September') and (num_days_in_month > 21):
	season = 'autumn'
elif (month_name.title() == 'December') and (num_days_in_month > 20):
	season = 'winter'

print(season)'''

# 38. Write a Python program to display astrological sign for given date of birth.
'''astro_sign = ''
birth_day = int(input("Enter birthday: "))
birth_month = input("Enter your birth month: ").lower().title()
if birth_month == 'December':
    astro_sign = 'Sagittarius' if birth_day < 22 else 'Capricorn'
elif birth_month == 'January':
    astro_sign = 'Capricorn' if birth_day < 20 else 'aquarius'
elif birth_month == 'February':
    astro_sign = 'aquarius' if birth_day < 19 else 'pisces'
elif birth_month == 'March':
    astro_sign = 'pisces' if birth_day < 21 else 'aries'
elif birth_month == 'Aprile':
    astro_sign = 'aries' if birth_day < 20 else 'taurus'
elif birth_month == 'May':
    astro_sign = 'taurus' if birth_day < 21 else 'gemini'
elif birth_month == 'June':
    astro_sign = 'gemini' if birth_day < 21 else 'cancer'
elif birth_month == 'July':
    astro_sign = 'cancer' if birth_day < 23 else 'leo'
elif birth_month == 'August':
    astro_sign = 'leo' if birth_day < 23 else 'virgo'
elif birth_month == 'September':
    astro_sign = 'virgo' if birth_day < 23 else 'libra'
elif birth_month == 'October':
    astro_sign = 'libra' if birth_day < 23 else 'scorpio'
elif birth_month == 'November':
    astro_sign = 'scorpio' if birth_day < 23 else 'sagittarius'


print("Your Astrological sign is :",astro_sign)'''

# Take 10 integers from keyboard using loop and print their average value on the screen.
'''i = 10
sum = 0
while i > 0:
    num = int(input("Enter the Number: "))
    sum = sum + num
    i -= 1

average = sum/10
print(average)'''

# Print multiplication table of 24, 50 and 29 using loop.
'''num = int(input("Enter the Nubmer: "))
i = 1
while i <= 10:
    print(str(num) + ' x '+ str(i) + " = " + str(num*i))
    i += 1
else:
    print('Done')'''

# 44. Write a Python program to construct the following pattern, using a nested loop number.
'''Expected Output:
1
22
333
4444
55555
666666
7777777
88888888
999999999
'''
'''for x in range(1, 10):
    for y in range(x):
        print(x,end='')
    print()
'''

# Exercise 1: Print First 10 natural numbers using while loop
'''i = 0
while i <= 10:
    print(i)
    i += 1'''

''' Exercise 2: Print the following pattern
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
'''
'''for x in range(1, 6):
    for y in range(1, x+1):
        print(y,end='')
    print()'''
# Exercise 3: Calculate the sum of all numbers from 1 to a given number.
'''num = int(input("Enter the Number: "))
sum = 0
for x in range(1, num+1):
    sum = sum + x
print(sum)'''

# Exercise 4: Write a program to print multiplication table of a given number
'''number = int(input("Enter the Number: "))
i = 1
while i <= 10:
    print(str(number) + " x " + str(i) + " = " + str(number*i))
    i += 1'''

# Exercise 5: Display numbers from a list using loop
#    The number must be divisible by five
#    If the number is greater than 150, then skip it and move to the next number
#    If the number is greater than 500, then stop the loop
'''numbers = [12, 75, 150, 180, 145, 525, 50]
for x in numbers:
    if x % 5 == 0 and x <= 150:
        print(x)
    elif x > 500:
        break'''
# Exercise 6: Count the total number of digits in a number
'''number = 71203948
i= 0
while number > 0:
    number = number // 10
    i += 1
print(i)'''

'''Exercise 7: Print the following pattern
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1'''
'''for x in range(5, 0, -1):
    for y in range(x, 0, -1):
        print(y, end=" ")
    print()'''
# Exercise 8: Print list in reverse order using a loop
'''list1 = [10, 20, 30, 40, 50]
for x in range(len(list1) - 1, -1, -1):
    print(list1[x])'''
# Exercise 9: Display numbers from -10 to -1 using for loop
'''for x in range(-10, 0, 1):
    print(x)
'''
# Exercise 10: Use else block to display a message “Done” after successful execution of for loop
'''for x in range(5):
    print(x)
else:
    print("Done!")'''
# Exercise 11: Write a program to display all prime numbers within a range
'''for x in range(25, 51):
    for y in range(2, x):
        if x % y == 0:
            break
    else:
        print(x)'''
# Exercise 12: Display Fibonacci series up to 10 terms
# 0, 1, 1, 2, 3, 5, 8, 13, 21
'''def Fibonacci_series(number):
    num_1 = 0
    num_2 = 1
    for x in range(number):
        print(num_1, end=" ")
        sum = num_1 + num_2
        num_1 = num_2
        num_2 = sum
Fibonacci_series(50)'''
# Exercise 13: Find the factorial of a given number
# using recurson
'''def factorial_of_number(num):
    if num == 1:
        return 1
    return num * factorial_of_number(num - 1)

print(factorial_of_number(5))'''
# Exercise 14: Reverse a given integer number
'''def reverse_integer(number):
    revers_num = ''
    while number > 0:
        reminder = number % 10
        revers_num = revers_num + str(reminder)
        number = number // 10
    return  revers_num

print(reverse_integer(int(input("Enter the number: "))))'''

# Exercise 15: Use a loop to display elements from a given list present at odd index positions
'''def display_odd_index_values(lst):
    for x in range(0, len(lst) + 1):
        if x % 2 != 0:
            print(lst[x])

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
display_odd_index_values(my_list)'''
# Exercise 16: Calculate the cube of all numbers from 1 to a given number
'''def calculate_cude (number):
    i = 1
    while i <= number:
        print("Current Number is :"+ str(i) + " and the cube is " + str(i**3))
        i += 1

print(calculate_cude(int(input("Enter the number: "))))'''

# Exercise 17: Find the sum of the series upto n terms
'''def find_sum_of_series(n, num):
    lst = []
    number_series = ''
    sum = 0
    for x in range(1, n+1):
        for y in range(x):
            number_series = number_series+str(num)
        lst.append(number_series)
        number_series = ''

    for x in lst:
        sum = sum + int(x)

    return sum

print(find_sum_of_series(int(input("Enter the number: ")), int(input("Enter the series num: "))))'''

'''Exercise 18: Print the following pattern
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
'''
'''def make_pattern():
    pattern = ''
    start, end, step = 1,6,1
    for x in range(start, end, step):
        for y in range(x):
            pattern = pattern+'* '
        pattern = pattern+'\n'

    start, end, step = 4, -1, -1
    for x in range(start, end, step):
        for y in range(x):
            pattern = pattern+'* '
        pattern = pattern+'\n'


    return pattern

print(make_pattern())'''

# Write a while loop that adds all the numbers up to 100 (inclusive).
'''def number_sum ():
    sum = 0
    i = 1
    while i <= 100:
        sum = sum + i
        i += 1
    print(sum)

number_sum()'''

# Using while loop, if statement and str() function; iterate through the list and if there is a 100, print it with its index number. i.e.: "There is a 100 at index no: 5"
'''lst=[10, 99, 98, 85, 45, 59, 65, 66, 76, 12, 35, 13, 100, 80, 95]
for x in range(0, len(lst), 1):
    if lst[x] == 100:
        print("There is a 100 at index " + str(x))'''
# Using while loop and an if statement write a function named name_adder which appends all the
# elements in a list to a new list unless the element is an empty string: "".
'''new_lst = []
def name_adder(lst):
    i = 0
    while i < len(lst):
        if lst[i] != '':
            new_lst.append(lst[i])
        i += 1

    return new_lst

lst1=["Joe", "Sarah", "Mike", "Jess", "", "Matt", "", "Greg", '']
print(name_adder(lst1))'''

#This time inside a function named name_adder, write a while loop that stops appending items to the new list
# as soon as it encounters an empty string: "". And prints "There is an empty string and returns the new list."

'''new_lst = []
def name_adder(lst):
    i = 0
    while i < len(lst):
        if lst[i] != '':
            new_lst.append(lst[i])
        else:
            break
        i += 1

    return new_lst

lst1=["Sam", "", "Ben", "Olivia", "Alicia"]
print(name_adder(lst1))
'''

'''new_lst = [x for x in input("Enter: ").split(',')]
print(new_lst)'''

new_lst = [x for x in range(20) if x % 2 == 0]
print(new_lst)

new_lst = [x for x in range(100) if x % 2 == 0 if x % 5 == 0]
print(new_lst)

new_lst = [x if x % 2 == 0 else 'odd' for x in range(20)]
print(new_lst)

new_lst = str([x for x in range(30) if x % 2 == 0 if x % 5 == 0 if x % 10 == 0])
print(new_lst)

new_lst = ['even' if x % 2 == 0 else 'odd' for x in range(20)]
print(new_lst)















