'''course  = "python for beginnners"
print(course.upper())
print(course)
print(course.find("y"))
print(course.replace("python for beginnners", "nasir will become a python expert"))
print("python" in course)
x = bytes(5)
x = memoryview(x)

x = -5j + 3
print(x)

# string

x = "python is awesome"
print(x)
print('hello')
# multiline string
x = """my name is nasir.
i am a software engineer.
i do work in big heap technologies"""
print(x)
# Strings are Array
a = "hello,world"
print(a[5])
# looping through the string
a = 'hello my name nasir'
for item in a:
    print(item, end="")
print('\n')

# string length

ace = 'Hi how are you?'
print(len(ace))

# check string
txt = "The best things in life are free!"
if 'best' in txt:
    print('yes it is')
print('life' in txt)
print('best' not in txt)

# python - string slicing

txt = "The best things in life are free!"
print(txt[2:6])
print(txt[:10])
print(txt[0:])
print(txt[-5:-1])

# python - Modify string
# Upper case
txt = "The best things in life are free!"
print(txt.upper())
print(txt.lower())

# remove white space:
txt = " hello , wolrd! "
print(txt.strip())
'''

'''txt = "we Are The So-called"
# c,e,f,i,j,l,m,p,r,s,t,u,z
# c
print(txt.capitalize())
print(txt.casefold())
print(txt.center(20,'n'))
print(txt.count('W'))
# e
print(txt.encode())
print(txt.endswith(('d','r','e')))
print(txt.endswith('r'))
txt = "H\te\tl\tl\to"
print(txt.expandtabs(10))
'''
# f
'''txt = "this is fine exercises"
print(txt.find('na'))
print(txt.find('is', 5, 10))
txt = "this is {} fine {} exercises"
print(txt.format(2,3))
txt = "this is \"4\" fine exercises"
print(txt.format_map(4))
'''
# e
'''txt = "this is fine exercises"
print(txt.index('is'))
print(txt.isalnum())
txt = "CompanyX"
print(txt.isalpha())
txt = "u300"
print(txt.isdecimal())

txt = "this is fine exercises"
print(txt.isdigit())
txt = "thisisfineexercises2_"
print(txt.isidentifier())
txt = "this is fine exercises"
print(txt.islower())
print("-----------------------------------")
a = "56890"
b = "\u00B2" #unicode for &sup2;
c = "10km2"
d = "-1"
e = "1.5"

print(a.isnumeric())
print(b.isnumeric())
print(c.isnumeric())
print(d.isnumeric())
print(e.isnumeric())

print('------------after numeric----------')
txt1 = "this is \r fine exercises"
print(txt1.isprintable())
txt = "Demo23"
print(txt.isprintable())

txt = " "
print(txt.isspace())

txt = "This Is Fine Exercises"
print(txt.istitle())

print(txt.isupper())

myTuple = ("John", "Peter", "Vicky")
x = ','.join(myTuple)
print(x)

mylst = ['nasir','sana','khadija','haris']
print(','.join(mylst))

mydict = {'name':'nasir','coutry':'pakistan'}
print('test'.join(mydict))

print('-------------L methods-----------')
txt = "nasir"
txt2 = 'this is awesome to work on python'
x = txt.ljust(6)
print(txt.ljust(20), "nasir")

txt2 = 'this is awesome to work on python'
print(txt2.lower())
print(txt2.strip('python'))

y = txt2.maketrans('t','b')
print(txt2.translate(y))

txt = "I could eat bananas all day"
print(txt.partition('bananas'))

print(txt.replace('bananas','mangoes'))
print(txt.rfind('a'))
print(txt.rpartition('eat'))
txt = "I could eat \n bananas all day"
print(txt.splitlines())

txt = " I could eat bananas all day "
print(txt.rstrip('a'))

txt = " I could eat bananas All Day "
print(txt.strip().swapcase())

print(txt.zfill(30))
'''
# Exercise 1A: Create a string made of the first, middle and last character
'''str1 = "James"
result_str = ''
result_str = result_str+str1[0]
result_str = result_str+str1[round(len(str1)/2)]
result_str = result_str+str1[-1]
print(result_str)'''
# Exercise 1B: Create a string made of the middle three characters
'''def string_function(string):
    middle_index = int(len(string)/2)
    result_string = string[middle_index-1:middle_index+2]
    return result_string

print(string_function("JhonDipPeta"))
print(string_function("JaSonAy"))'''
# Exercise 2: Append new string in the middle of a given string
'''def append_string_func(str1, str2):
    middle_index = int(len(str1)/2)
    result_string = str1[:middle_index] + str2 + str1[middle_index:]
    return result_string

print(append_string_func('Ault', 'Kelly'))'''
# Exercise 3: Create a new string made of the first, middle, and last characters of each input string
'''def return_first_middle_last_char(str1, str2):
    middle_index_str2 = int(len(str2)/2)
    middle_index_str1 = int(len(str1) / 2)
    new_string = str1[0] + str2[0] + str1[middle_index_str1] + str2[middle_index_str2] + str1[-1] + str2[-1]
    return new_string

print(return_first_middle_last_char('America', 'Japan'))

'''

# Exercise 4: Arrange string characters such that lowercase letters should come first
'''def arrange_string_in_lowercase(str):
    lower_case_str = ''
    upper_car_str = ''
    for string in str:
        if string.islower():
            lower_case_str = lower_case_str+string
        else:
            upper_car_str = upper_car_str + string
    return  lower_case_str + upper_car_str

print(arrange_string_in_lowercase('myISnaSiR'))'''

# Exercise 5: Count all letters, digits, and special symbols from a given string
'''def count_digits_chars_symbols (string):
    digit, chars, special_symbol = 0, 0, 0
    for letter in string:
        if letter.isdigit():
            digit +=1
        elif letter.isalpha():
            chars += 1
        else:
            special_symbol += 1

    return chars ,digit,special_symbol

print("digits: ", count_digits_chars_symbols('P@#yn26at^&i5ve'))'''

# Exercise 6: Create a mixed String using the following rules
# Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1,
# then the last char of s2, Next, the second char of s1 and second last char of s2, and so on.
# Any leftover chars go at the end of the result.
'''def mixed_strings(str1, str2):
    result_str = ''
    i = 0
    while True:
         # index_str2 = i + 1
        result_str += str1[0]
        result_str += str2[-1]
        str1 = str1.replace(str1[0], '')
        str2 = str2.replace(str2[-1], '')
        if str1 == '' and str2 != '':
            result_str += str2
            break
        elif str1 != '' and str2 == '':
            result_str += str1
            break
        elif str1 == '' and str2 == '':
            break

    return result_str

print(mixed_strings('Abcqdf', 'Xyzw'))'''

# Exercise 7: String characters balance Test
# Write a program to check if two strings are balanced.
# For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2.
# The character’s position doesn’t matter.
'''def is_strings_balanced (str1, str2):
    is_balanced = False
    for letter_str1 in str1:
        for letter_str2 in str2:
            if letter_str1 == letter_str2:
                is_balanced = True
                break
            else:
                is_balanced = False


    return is_balanced'''

'''def is_strings_balanced (str1, str2):
    is_balanced = False
    for letter_str1 in str1:
        if letter_str1 in str2:
            is_balanced = True
            continue
        else:
            is_balanced = False

    return is_balanced


print(is_strings_balanced('Ynw', 'PYnativew'))'''

# Exercise 8: Find all occurrences of a substring in a given string by ignoring the case
# Write a program to find all occurrences of “USA” in a given string ignoring the case.
'''def check_occurrences (str1, str2):
    return str2.count(str1)

print(check_occurrences('USA'.lower(), 'Welcome to USA. usa usa awesome, isnt it?'.lower()))

'''
# Exercise 9: Calculate the sum and average of the digits present in a string
# Given a string s1, write a program to return the sum and average of the digits that appear in the string,
# ignoring all other characters.
'''def calculate_sum_average (str):
    sum = 0
    average = 0
    num_of_digits = 0
    for letter in str:
        if letter.isdigit():
            num_of_digits += 1
            sum = sum + int(letter)

    average = sum/num_of_digits

    return average, sum

average, sum = calculate_sum_average('PYnative29@#8496')
print('Average: ', average)
print('Sum: ', sum)'''

# Exercise 10: Write a program to count occurrences of all characters within a string
'''def count_occurrences_all_chars (str):
    new_dict = {}
    for letter in str:
        new_dict[letter] = str.count(letter)

    return new_dict

print(count_occurrences_all_chars('Apple'))'''

# Exercise 11: Reverse a given string
'''def reverse_a_string(str):
    new_reverse_string = ''
    while True:
        new_reverse_string += str[-1]
        str = str.replace(str[-1], '')
        if str == '':
            break
    return new_reverse_string

print(reverse_a_string('PYnative'))'''

# Exercise 12: Find the last position of a given substring
'''str1 = "Emma is a data scientist who knows Python. Emma works at google."
print('Last occurrence of Emma starts at index ' + str(str1.rfind('Emma')))
'''
# Exercise 13: Split a string on hyphens
'''str1 = 'Emma-is-a-data-scientist'
new_string = str1.split('-')
for x in new_string:
    print(x)'''

# Exercise 14: Remove empty strings from a list of strings
'''str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
for item in str_list:
    if item == '' or item == None:
        str_list.remove(item)
print(str_list)'''
import string
# Exercise 15: Remove special symbols / punctuation from a string
'''str1 = "/*Jon is @developer & musician"
new_str = str1.translate(str.maketrans('', '', string.punctuation))
print(new_str)'''
# Exercise 16: Removal all characters from a string except integers
'''str1 = 'I am 25 years and 10 months old'
res = ''.join([item for item in str1 if item.isdigit()])
print(res)'''
# Exercise 17: Find words with both alphabets and numbers
'''str1 = "Emma25 is Data scientist50 and AI Expert"
new_str_lst = str1.split(' ')
for temp in new_str_lst:
    if any(item.isalpha() for item in new_str_lst) and any(item.isdigit() for item in new_str_lst):
        new_str_lst.append(temp)
print(new_str_lst)'''

# Exercise 18: Replace each special symbol with # in the following string
'''def replace_specialsymbol (str, symbol):
    for item in string.punctuation:
        str = str.replace(item, symbol)
    return str

print(replace_specialsymbol('/*Jon is @developer & musician!!', '#'))
print(string.punctuation)'''

# Python program to check whether the string is Symmetrical or Palindrome
# symmetric string --> khokho
# palindrom string --> amaama
'''def palindram(a):
    start = 0
    mid = (len(a)-1)//2 # 2 aamama
    end = len(a) - 1 # 5
    flag = True
    print(mid)
    while start <= mid:
        if a[start] == a[end]:
            start += 1
            end -= 1
            flag = True
        else:
            flag = False
            break

    if flag:
        print('String is plindrom')
    else:
        print('String is not palindrom')

#palindram('amaaama')

def symmetric (a):
    n = len(a)

    if n % 2 != 0:
        mid = n // 2 + 1
        print(mid)
    else:
        mid = n // 2
   # mid = n // 2

    flag = 0
    # amaaama
    start = 0
    start1 = mid
    while start < mid and start1 < n:
        if a[start] == a[start1]:
            start += 1
            start1 += 1
            flag = 1
        else:
            flag = 0
            break
    if flag == 0:
        print('String is not symmetric')
    else:
        print('String is symmytric')

string = input('Enter the String: ')
symmetric(string)
palindram(string)
'''

# Reverse words in a given String in Python
# We are given a string and we need to reverse words of a given string
# Input : str =" geeks quiz practice code"
# Output : str = code practice quiz geeks
# Input : str = "my name is laxmi"
# output : str= laxmi is name my

'''string = "geeks quiz practice code"
reverse = string.split()[::-1]
print(' '.join(reverse))

print('------2nd Approach-------')
def rev_sentence(str):
    words = str.split(' ')
    reverse_sentence = ' '.join(reversed(words))
    return reverse_sentence

print(rev_sentence('geeks quiz practice code'))'''

# Ways to remove i’th character from string in Python
'''test_str = "GeeksForGeeks"
new_str = ''
for i in range(len(test_str)):
    if i != 2:
        new_str += test_str[i]
print ("The string after removal of i'th character : " + new_str)

print('------2nd Approach-------')
test_str = "GeeksForGeeks"
test_str = test_str.replace('e', '', 2)
print(test_str)'''

# Find length of a string in python (6 ways)
'''print('------1st Way-------')
str = "geeks"
print(len(str))
print('------2nd Way-------')
def findlen(str):
    count = 0
    for i in str:
        count += 1
    return count
str = "geeks"
print(findlen(str))
print('------3rd Way-------')
def findLen(given_str):
    count = 0
    while given_str[count:]:
        count += 1
    return count
str = "geeks"
print(findLen(str))
print('------4th Way-------')
def findLen3(give_str):
    if not give_str:
        return 0
    else:
        some_random_str = ','
        return (some_random_str.join(give_str)).count(some_random_str) + 1
str = "geeks nas"
print(findLen3(str))
print('------5th Way-------')
import functools

def findLen4(given_str):
    return functools.reduce(lambda x,y: x+1, given_str,0)
str = "geeks"
print(findLen4(str))
print('------6th Way-------')
def findLen5 (given_str):
    return sum([1 for i in given_str])
str = "geeks"
print(findLen5(str))
'''
# Python – Avoid Spaces in string length
# Given a String, compute all the characters, except spaces.
'''print('-----1st Way------------')
def findLen_avoid_spaces(give_str):
    len_count = sum([not char.isspace() for char in give_str])
    return len_count
test_str = 'geeksforgeeks 33 is   best'
print(findLen_avoid_spaces(test_str))

print('-----2nd Way------------')
def find_len6(give_str):
    #res = sum(map(len, give_str.split()))
    res = sum(map(len, give_str.split()))
    return res

test_str = 'geeksforgeeks 33 is   best'
print(find_len6(test_str))'''

# Python program to print even length words in a string
'''print('---1st way---')
n="This is a python language"
lst = n.split(' ')
for x in lst:
    if len(x) % 2 == 0:
        print(x, end=" ")
print()
print('---2nd way---')
n="This is a python language"
lst = n.split(' ')
print([x for x in lst if len(x) % 2 == 0])

print('---3rd way---')
n="This is a python language"
lst = n.split(' ')
l=list(filter(lambda x: (len(x)%2==0),lst))
print(l)
print('---4th way---')
n="This is a python language"
lst = n.split(' ')
print([x for i,x in enumerate(lst) if len(x)%2==0])'''

# Python – Uppercase Half String
# using len, loop, upper()
'''test_str = 'geeksforgeeks'
half_index = len(test_str) // 2
new_string = ''
for idx in range(len(test_str)):
    if half_index <= idx:
        new_string += test_str[idx].upper()
    else:
        new_string += test_str[idx]
print(new_string)

# Method #2 : Using list comprehension + join() + upper()
test_str = 'geeksforgeeks'
half_index = len(test_str) // 2
new_string = ''
new_string = ''.join([test_str[x] if x < half_index else test_str[x].upper() for x in range(len(test_str))])
print(new_string)

# Method#3: Using String slicing and upper()
test_str = 'geeksforgeeks'
new_str1 = test_str[:(len(test_str)//2)]
new_str2 = test_str[len(test_str)//2:]
print(new_str1)
print(new_str2)
final_string = new_str1 + new_str2.upper()
print(final_string)
'''

# Python program to capitalize the first and last character of each word in a string
'''Approach:

    Access the last element using indexing.
    Capitalize the first word using title() method.
    Then join the each word using join() method.
    Perform all the operations inside lambda for writing the code in one-line.'''

'''s = "welcome to geeksforgeeks"
x = s[1:-1]
print(x)
lst = s.split(' ')
new_lst = []
for i in lst:
    x = i[0].upper()+i[1:-1]+i[-1].upper()
    new_lst.append(x)
print(' '.join(new_lst))

# using lambda finction
def word_both_cap(str):
    new_str = ' '.join(list(map(lambda s: s[:-1]+s[-1].upper(), s.title().split(' '))))
    return new_str
s = "welcome to geeksforgeeks"
print(word_both_cap(str))


lst = s.split(' ')
new_str = ' '.join([s[0].upper()+s[1:-1]+s[-1].upper() for s in lst])
print(new_str)'''

# Python program to check if a string has at least one letter and one number

'''def check_string(str):
    flag_i = False
    flag_c = False
    for i in string:
        if i.isalpha():
            flag_c = True
        if i.isdigit():
            flag_i = True
    return flag_i , flag_c

string = '$%^@3%4'
flag_i, flag_c = check_string(string)
print(flag_i, flag_c)
'''
# Python | Program to accept the strings which contains all vowels
'''def check_string(string):
    string = string.lower()
    vowels = set('aeiou')
    print(vowels)
    s = set({})
    for i in string:
        if i in vowels:
            s.add(i)
    print(s)
    if len(s) == len(vowels):
        print("String is Accepted")
    else:
        print("String is not Accepted")

check_string("SEEquoiaL")
check_string("geeksforgeeks")

# Alternate Implementation Using count():
def check_string(string):
    string = string.replace(' ', '')
    string = string.lower()
    vowals = [string.count('a'), string.count('i'), string.count('o'), string.count('u'), string.count('e')]

    if vowals.count(0) > 0:
        return 'String is not Accepted'
    else:
        return 'String is Accepted'

string = "SEEquoiaL"
string2 = 'geeksforgeeks'
print(check_string(string))
print(check_string(string2))

# Alternate Implementation 2.0 : using set

def check_string3(string):
    if len(set(string.lower().intersection('aeiou'))) >= 5:
        return 'String is Accepted'
    else:
        return 'String is not Accepted'
string = "SEEquoiaL"
string2 = 'geeksforgeeks'
print(check_string3(string))
print(check_string3(string2))'''

# Python | Count the Number of matching characters in a pair of string
'''def count_matching_strings(str1, str2):
    str1 = set(str1)
    str2 = set(str2)
    matching_num = set({})
    matching_num = str1.intersection(str2)
    print(matching_num)
    return len(matching_num)
print(count_matching_strings('abcdefwerrdss', 'defghiaskhfkdjshfkjlehfiewflksdhf'))
print(count_matching_strings('aabcddekll12@', 'bb22ll@55k'))

# Approach 2: Using search method
import re
ip1 = "geeks"
ip2 = "geeksonly"
c = 0;
for i in ip1:
    if re.search(i, ip2):
       c += 1
print(c)

ip1 = "geeks"
ip2 = "geeksonly"

print(re.search('[ge]', ip2))'''

# Python program to count number of vowels using sets in given string
'''def find_vowals(string):
    vowals = set('aeiouAEIOU')
    count = 0
    for char in string:
        if char in vowals:
            count += 1
    return count
print('No of vowals: ',+find_vowals('GeeksforGeeks'))
print('No of vowals: ',+find_vowals('Hello World'))'''

# Remove all duplicates from a given string in Python
'''from collections import OrderedDict
def remove_dup_without_order(string):
    return ''.join(set(string))
print(remove_dup_without_order('geeksforgeeks'))

# remove dup in order
def remove_dup_with_order(string):
    dict = OrderedDict.fromkeys(string)
    return ''.join(dict)

print(remove_dup_with_order('my name is nasir'))

# Method 2: using forloop
def remove_dup (string):
    string = set(string)
    print('without order: ', ''.join(string))

remove_dup('geeksforgeeks')'''

# Python – Least Frequent Character in String
'''test_str = "GeeksforGeeks"
all_freq = {}
for char in test_str:
    if char in all_freq:
        all_freq[char] += 1
    else:
        all_freq[char] = 1
least_freq = min(all_freq, key=all_freq.get)
max_freq = max(all_freq, key=all_freq.get)
print(least_freq)
print(max_freq)

#  Method 2 : Using collections.Counter() + min()
from collections import Counter
test_str = "GeeksforGeeks"
all_freq = Counter(test_str)
print(all_freq)
least_freq = min(all_freq, key=all_freq.get)
print ("The minimum of all characters in GeeksforGeeks is : " + str(least_freq))
'''
# Python | Maximum frequency character in String. Done with max() method

# Python – Odd Frequency Characters
# using defaultdict() and list comprehnsion
'''from collections import defaultdict
def odd_freq_character (string):
    cntr = defaultdict(int)
    for chr in string:
        cntr[chr] += 1

    odd_char = [key for key, value in cntr.items() if value % 2 != 0]
    return odd_char


string = 'geekforgeeks is best for geeks'
print(odd_freq_character(string))

# using counter()
from collections import Counter
string = 'geekforgeeks is best for geeks'

dict_count = [key for key, value in Counter(string).items() if value % 2 != 0]
print(dict_count)

# Using Count method:
string = 'geekforgeeks is best for geeks'
lst = []
for i in string:
    if string.count(i) % 2 != 0:
        lst.append(i)
print(list(set(lst)))
'''
# Python – Specific Characters Frequency in String List:
# using Count() + join() + dictionary comprehension
'''from collections import Counter
test_list = "geeksforgeeks is best for geeks"
chr_list = ['e', 'b', 'g']

res = {key:value for key, value in dict(Counter(test_list)).items() if key in chr_list}
print(res)'''

# Python | Frequency of numbers in String
# using findall() and len()
'''import re
test_str = "geeks4feeks is No. 1 4 geeks"
res = len(re.findall(r'\d+', test_str))
print(res)

# using findall() and sum()

test_str = "geeks4feeks is No. 1 4 geeks"
res = sum(1 for _ in re.findall(r'\d+', test_str))
print(res)'''

# Program to check if a string contains any special character
'''import re

def check_string_contain_num(str):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

    if regex.search(str) == None:
        print('String is acceptable')
    else:
        print('string in not accept')

test_string = "Geeks$For$Geeks"
string2 = "GeeksForGeeks"
check_string_contain_num(test_string)
check_string_contain_num(string2)

# using loop
test_string = "GeeksFor#Geeks"
count = 0
for char in test_string:
    if char in string.punctuation:
        count += 1
        break
    else:
        count = 0
if count > 0:
    print('string is not acceptable')
else:
    print('String is acceptable')
'''

# Find words which are greater than given length k
'''def find_words_len_greater(given_str, length):
    greater_words = ''
    str_lst = given_str.split(' ')
    for word in str_lst:
        if len(word) > length:
            greater_words += word + ' '
    return greater_words

str = "hello geeks for geeks is computer science portal"
print(find_words_len_greater(str, 4))

# using list comprehension
def find_words_len_greater2(given_str, length):
    greater_words = [words for words in given_str.split(' ') if len(words) > length]
    return ' '.join(greater_words)
str = "string is fun in python"
print(find_words_len_greater2(str, 3))

# Using Lambda function
n="hello geeks for geeks is computer science portal"; l=4
s = n.split(' ')
greater_words = list(filter(lambda x: (len(x) > l), s))
print(' '.join(greater_words))

# Method: Using the enumerate function
sentence = "hello geeks for geeks is computer science portal"
length = 4
s = sentence.split(' ')
print(' '.join([a for i,a in enumerate(s) if len(a) > length]))

for i, x in enumerate(s):
    print(x)

'''

# Python | Find all close matches of input string from a list
'''from difflib import get_close_matches
def closematch(pattern, word):
    print(get_close_matches(word, pattern))

word = 'appel'
patterns = ['ape', 'apple', 'peach', 'puppy']
closematch(patterns, word)'''

# Python program to find uncommon words from two Strings
'''A = "Geeks for Geeks"
B = "Learning from Geeks for Geeks"
# Output : ['Learning', 'from']
A_set = set(A.split(' '))
b_set = set(B.split(' '))

x = A_set.symmetric_difference(b_set)
print(x)'''

# Python | Swap commas and dots in a String
'''test_str = '14, 625, 498.002'
test_str = test_str.replace(',', 't')
test_str = test_str.replace('.', ',')
test_str = test_str.replace('t', '.')
print(test_str)
'''

'''filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = []
for name in filenames:
    if name.endswith('hpp'):
        name = name.replace('hpp', 'h')
    newfilenames.append(name)

print(newfilenames)'''

'''animal = "Hippopotamus"
print(animal[-5])



Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

Rorys_guests.update(Taylors_guests)

Taylors_guests.update(Rorys_guests)
print(Rorys_guests)
print(Taylors_guests)'''


'''print(dir(""))
print(help(""))'''

'''class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.bottom = bottom
        self.top = top
        self.current = current
    def __str__(self):
        return "Current floor:{}".format(self.current)
    def up(self):
        """Makes the elevator go up one floor."""
        if self.current < 10:
            self.current += 1
    def down(self):
        """Makes the elevator go down one floor."""
        if self.current > 0:
            self.current -= 1
    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        self.current = floor

elevator = Elevator(-1, 10, 0)



elevator.go_to(5)
print(elevator)

'''


'''class Animal:
    name = ""
    category = ""

    def __init__(self, name):
        self.name = name

    def set_category(self, category):
        self.category = category


class Turtle(Animal):
    pass

turtle = Turtle("turtle")
turtle.set_category("reptile")

print(turtle.category)

class Snake(Animal):
    category = ""
snake_obj = Snake('snake')
snake_obj.set_category('reptile')
print(snake_obj.category)

'''

'''def get_event_date(event):
  return event.date

def current_users(events):
  events.sort(key=get_event_date)
  machines = {}
  for event in events:
    if event.machine not in machines:
      machines[event.machine] = set()
    if event.type == "login":
      machines[event.machine].add(event.user)
    elif event.type == "logout" and event.user in machines[event.machine]:
        print(machines.values())
        machines[event.machine].remove(event.user)
  return machines

def generate_report(machines):
  for machine, users in machines.items():
    if len(users) > 0:
      user_list = ", ".join(users)
      print("{}: {}".format(machine, user_list))


class Event:
  def __init__(self, event_date, event_type, machine_name, user):
    self.date = event_date
    self.type = event_type
    self.machine = machine_name
    self.user = user

events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'logout', 'mailserver.local', 'chris'),
]

users = current_users(events)
print(users)

'''

from collections import Counter

# initializing string
test_str = 'The Project Gutenberg eBook of To the lights, by Roy Norton ' \
           'This eBook is for the use of anyone anywhere in the United States and ' \
           '' \
           'hello'
# printing original string
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
'''for x in punctuations:
    if x in test_str:
        test_str = test_str.replace(x, '')'''

test_str = test_str.translate(str.maketrans('', '', punctuations))
test_str = test_str.lower()
print(test_str)
my_list = [x for x in test_str.split(' ') if x not in uninteresting_words]
freq_dict = {}
'''for word in my_list:
    if word not in freq_dict:
        freq_dict[word] = 0
    freq_dict[word] += 1'''
freq_dict = dict(Counter(my_list))
print(freq_dict)


# using collections.Counter() + max() to get
# Maximum frequency character in String

# Here are all the installs and imports you will need for your word cloud script and uploader widget





