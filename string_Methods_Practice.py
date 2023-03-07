# c e f i j l m p r s t u z
# c
txt = "learning python is awesome"
print(txt.capitalize()) # Convert 1st letter of string to upper case

txt = "IT'S BEEN TWO WEEKS, I AM LEARNING TO THE PYTHON"
print(txt.casefold()) # Convert string to lower.

txt = "learning python is awesome"
print(txt.center(100)) # Return a centred string

txt = "learning python is awesome"
print(txt.count('a')) # return the number of time s specific value occur in the string.
print(txt.count('python'))

print('----------E---------------------')
# e
txt = "learning python is awesome"
print(txt.encode()) # Return encoded version of a string
print(txt.endswith('e')) # Return true if a string ends with a specific value
print(txt.endswith(('me', 'me','awesome','is')))

txt = "h\te\tl\tl\to"
print(txt.expandtabs(20)) # Set the tab size of a string

print('------------F-----------------')
txt = "learning python is awesome"
print(txt.find('y')) # Search the string for specific value and return the position where it was found
print(txt.find('python'))
print(txt.find('na'))

txt = "learning python is awesome and it's been {} weeks, i learning python and targeting {} month to complete"
print(txt.format(2, 4)) # Format the specific value in to the string
print(txt.format(3,4,5,6,7))
##dicstionary = {'weeks': 2, 'months': 4}
##txt = "learning python is awesome and it's been {} weeks"
##print(txt.format_map(6))

print('----------------I--------------------')

txt = "learning python is awesome and it's been 2 weeks, i learning python and targeting 4 month to complete"
print(txt.index('e')) # search for specific character and return its position where it was found
print(txt.index('and'))
#print(txt.index('nas'))
txt = 'W123456789'
print(txt.isalnum()) # Return True if all charcaters in string are Alphanumeric. Note: space is not alphanumeric
txt = 'World'
print(txt.isalpha()) # Return True if all character in the string are Alphabet
# Example of characters that are not alphabet letters: (space)!#%&? etc.
txt = '12345'
print(txt.isdecimal()) # Return True if all characters in the string are decimals. it is use unicode

a = "\u0030" #unicode for 0
b = "\u0047" #unicode for G
print(a.isdecimal())
print(b.isdecimal())

txt = "12345678"
print(txt.isdigit()) # Return true if All characters in the string are digits

txt = "learning python is awesome and it's been 2 weeks, i learning python and targeting 4 month to complete"
print(txt.isidentifier()) # Return True if a string is an Identifier
print(txt.isidentifier()) # True

txt = "nasir_9026"
txt = "learning python is awesome and it's been 2 weeks, i am learning it"
print(txt.islower()) # Return True if all characters in the string are lower case
txt = '1234567'
print(txt.isnumeric()) # Return true if all characters in the string are numeric

txt = "learning python is awesome and it's been 2 weeks, i am learning it"
print(txt.isprintable()) # Return True if string is printable. not contain \n,\r,\',\\
txt = " "
print(txt.isspace()) # Return true if a string a a whitespace

txt = "Learning Python Is Awesome And It's Been 2 Weeks, I Am Learning It"
print(txt.istitle()) # Return True if first character of every word is capital in string anf rest charcaters are lower

print(txt.isupper()) # Return true if all character in a string are upper case

print("--------------J-------------")
lst = ['python', 'is', 'awesome']
x = ' '.join(lst) # join the string of Iterable objects like list,tuples,dictionary
print(x)

dictionary = {'language': 'python', 'use': 'web develpement'}
x = ' '.join(dictionary)
print(x)

print('-----------L-------------')
txt = "python is awesome"
print(txt.ljust(20))

txt = "PYTHON IS AWESOME"
print(txt.lower()) # Convert the string in lower

txt = "python is awesome"
print(txt.lstrip('python')) # Return the left trim version of string

print('---------------M---------')
txt = "python is awesome" #pycharm
a = 'ton'
b = 'car'
c = ' is awesme'
my_trans = txt.maketrans(a,b,c)
print(txt.translate(my_trans))

print("------------M-------------")
txt = "python is awesome"
print(txt.partition('is')) # divide the string in tuple

print('-----------R-------------')
txt = "python is awesome"
print(txt.replace('thon is awesome', 'charm')) # Replace the specific part of string to given one

print(txt.rfind('e')) # Search string for a value and return the last position where it was found
print(txt.rindex('e')) # search for a value and return it last position where it was found
print(txt.rjust(50, 'n')) # Returns a right justified version of the string
print(txt.ljust(50))
print(txt.rpartition('is')) #Returns a tuple where the string is parted into three parts
print(txt.rsplit('is')) # Splits the string at the specified separator, and returns a list
print(txt.split('is'))
print(txt.rstrip('e')) # Return right trimmed version of string
print(txt.lstrip(txt[:5]))
print(txt.strip('p'))

txt = "python \r is awesome"
print(txt.splitlines()) # Splits the string at line breaks and returns a list

txt = "python is awesome"
print(txt.swapcase()) # Swaps cases, lower case becomes upper case and vice versa
print(txt.startswith('y'))
print(txt.startswith(('p','y','s')))

print(txt.title()) # convert the first character of every word in upper case in a string
print(txt.upper())

print(txt.zfill(30)) # Fills the string with a specified number of 0 values at the beginning



