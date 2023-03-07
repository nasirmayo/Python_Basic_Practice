
x = lambda a: a + 10

print(x(5))

x = lambda a,b,c : a+b+c
print(x(2,3,4))

def my_function(n):
    return lambda a: a*n

my_value = my_function(3)
print(my_value(4))

my_triple_value = my_function(3)
print(type(my_triple_value))
print(my_value(11))
print(my_triple_value(11))