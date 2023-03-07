my_set = {'apple', 'mango', 'cherry'}
print(my_set)

# do not Allow duplication
my_set = {'apple', 'apple', 'mango', 'mango'}
print(my_set)

# set construct

my_set = set(('apple', 'mango', 'cherry'))
print(my_set)

# accessing the set
my_set = {'apple', 'mango', 'cherry', 'banana'}
for x in my_set:
    print(x)

if 'na' in my_set:
    print('Yes banana is in the this Set')
else:
    print('its not in there')

# Add 1 item in set
my_set = {'apple', 'mango', 'cherry', 'banana'}
my_set.add('Gauva')
print(my_set)

# Add any iterable in set

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya", "cherry"}
thisset.update(tropical)
print(thisset)

my_lst = ['nasir', 'irfan']
thisset.update(my_lst)
print(thisset)

# Remove items from Set: two functions used, remove(), discard()
thisset.remove('cherry')
print(thisset)

thisset.discard('banana')
print(thisset)

for item in thisset:
    print(item)


thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya", "cherry"}
s3 = thisset.union(tropical)
print(s3)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)
print(x)


z = x.symmetric_difference(y)
print(z)

# diffirence function

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = y.difference(x)
print(z)

x.difference_update(y)
print(x)
x.add('nasir')
print(x)
print(x.isdisjoint(y))

# is subset

x = {'a','b','c'}
y = {'e', 't', 'a', 'w', 'b', 'd', 'c'}
z = {'w', 'r', 'z'}
print(x.issubset(y))
print(x.issubset(z))


x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
print(x.issubset(y))
print(x.issuperset(y))
print(y.issuperset(x))

x = {'apple', 'banana', 'google', 'cherry', 'microsoft'}
x.discard('banana')
print(x)
x.discard('banana')
print(x)
x.remove('google')
print(x)
x = {'apple', 'banana', 'google', 'cherry', 'microsoft'}
x.pop()
print(x)

# pop in list
x = ['apple', 'banana', 'google', 'cherry', 'microsoft']
x.pop(4)
print(x)