import sys

# first funstion

def my_function():
    print("this is my first function in python")

my_function()

# functions with Arguments
def my_funtion(fname):
    print(fname)

my_funtion("nasir")

# a function with the 2 args:
def my_function_2(fname,lname):
    print(fname,lname)

my_function_2("muhammad","nasir")

# Arbitrary Arguments, *args. Tuple go as args: If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

def my_function_3(*my_family):
    print(my_family)
    print("my daughter name is", my_family[1])
    print("my son name is: ",my_family[2])
    print("my wife name is: ",my_family[3])
    print("my mother: ",my_family[0])
my_function_3("mom","khadija","haris","sana","nasir")

# Keyword Arguments: You can also send arguments with the key = value syntax.

def my_function_4(child3, child4, child1,child2):
    print("my youngest child is:",child4)

my_function_4(child1='khadija', child2='haris',child3='fatima',child4='amir')

# Arbitrary Keyword Arguments, **kwargs:If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

# Arbitrary Kword Arguments are often shortened to **kwargs in Python documentations.

def my_function_5(**my_family):
    print(type(my_family))
    print("the oldest kids is",my_family["lname"])

my_function_5(fname = "M", lname = "nasir", surname = "mayo")

# Default Parameter Value

def my_function_6 (coutry = "norway"):
    print("my country is:",coutry)

my_function_6("india")
my_function_6("pakistan")
my_function_6()

# Passing a List as an Argument

def my_function_7(fruits):
    print(fruits)


fruit_lst = ["mango", 'apple','gauva','strawberry']

my_function_7(fruit_lst)

# Return Values

def my_function_8 (value):
    return value*3

print(my_function_8(3))

# The pass Statement

def my_function_9(value):
    print(value)

my_function_9(10)


# funtion Recursion:
print('----------------------------------------')
print(sys.getrecursionlimit())
sys.setrecursionlimit(5000)
print(sys.getrecursionlimit())

def try_recursion(k):
    if k > 0:
        result = k + (try_recursion(k - 1)) # 6 + 5 + 4 + 3 + 2 + 1
        print(result)
    else:
        result = 0;
        print(result)
    return result

try_recursion(6)



def my_finction_10():
    pass

def my_function_factorial(factorial_value):
   if factorial_value > 1:
       result = factorial_value * (my_function_factorial(factorial_value - 1))
   else:
       result = 1;



   return result


print(my_function_factorial(5))


# Hanoi game

'''def move (f,t):
    print("move disc from {} to {}!".format(f,t))

#move('A','B')

def moveViaw(f,v,t):
    move(f,v)
    move(v,t)

moveViaw('A','B','C')


def hanoi (n,f,v,t):
    if n == 0:
        pass
    else:
        hanoi(n-1,f,t,v)
        move(f,t)
        hanoi(n-1,v,f,t)

hanoi(4,'A','B','C')
'''