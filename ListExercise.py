'''names = ["nasir", "sarwar", "shahbaz", "Awais", "shahid"]
print(names)

print(names[0])
print(names[4])
print(names[-2])

names[0] = "muhammad nasir"
print(names)

print(names[0:3])
print(names)


num = [1, 2, 3, 4, 5, 6]
num.append(7)
print(num)

num.insert(0, 9)
print(num)

num.remove(3)
print(num)

#num.clear()
#print(num)

print(1 in num)

print(10 in num)

print(len(num))

list1 = [1,2,3,4,5,6,7,8]
print(list1[:7])
print(list1[2:8])
print(list1[:7:3])
'''
'''print(list1[-6:-1])
print(list1[1:])
print(list1)

# Dictionaries

d = {'int_value':3, 'str_value':'hello', 'boolean Value': True}
print(d)
print(d['int_value'])
print(len(list1))
print(len(d))'''

lst = ['apple', 'orange','cherry', 'banana', 'mango','orange']
print(lst)
print(lst[0])
# Changeable
lst[0] = 'mango'
print(lst)
lst[0:2] = ['banana','cherry']
print(lst)
lst[:3] = ['banana','cherry', 'orange']
print(lst)
lst[:3] = ['banana']
print(lst)
lst = [1,2,3,4,5]
lst[1:] = [8,9,10]
print(lst)
lst[:len(lst)] = [10]
print(lst)

lst = [1,2,3,4,5,6,7,8,9]
print(lst[-5:-1])

lst = [True,True,False,False,True,True]
print(lst)
lst[1] = 'nasir'
print(lst)
lst[0:2] = [False,'nasir',True]
print(lst)

print("-----------List Comprehension----------")

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
[print(x) for x in fruits]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

'''for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

newlist = [x for x in fruits if 'a' in x]
print(newlist)
'''

print('-----------list comrehension---------')
newlist = [x for x in fruits if x != 'apple']
print(newlist)
newlist = [x if x != 'apple' else 'nasir' for x in fruits]
print(newlist)

newlist = [x for x in fruits]
print(newlist)

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

newlist = ['hello' for x in fruits]
print(newlist)