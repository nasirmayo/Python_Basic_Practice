lst = ['apple','mango','orange','banana']

lst.append('Gauva')
print(lst)

lst.clear()
print(lst)

lst2 = []
lst = ['apple','mango','orange','banana','apple']
lst2 = lst.copy()
print(lst2)
print(lst)
print(lst.count('apple'))

lst2 = ['nasir','moeez','irfa']
lst.extend(lst2)
print(lst)

print(lst.index('banana'))

lst = ['apple','mango','orange','banana','apple']
lst.insert(3,'gauva')
print(lst)

lst.pop(2)
print(lst)

lst.remove('apple')
print(lst)

lst.reverse()
print(lst)
lst = ['apple','mango','orange','banana','apple']
lst.sort()
print(lst)
def myFunction(e):
    return len(e)
print(lst.sort(key=myFunction))

print("----------delete-----------")
lst = ['apple','mango','orange','banana','apple']
del lst[0]
print(lst)

print(lst.count('apple'))

