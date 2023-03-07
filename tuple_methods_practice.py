fruits = ('apple','mango','cherry')

# access tuple
print(fruits[0])
print(fruits.count('apple'))

print(fruits[1:2])

# add item
lst = list(fruits)
lst[0] = 'nasir'
lst.append('banana')
fruits = tuple(lst)
print(fruits)

# Add tuple with tuple

vegi = ('tomatos','carrot')

tuple_sum = fruits+vegi
print(tuple_sum)

fruits1 = ('apple',)
print(fruits1)

# unpacking tuples
fruits = ('apple','mango','cherry')
(green,yellow,red) = fruits
print(green)
print(yellow)
print(red)
print("---------Loop--------")
for item in fruits:
    print(item)

print('---------by index--------')
for x in range(len(fruits)):
    print(fruits[x])


print(fruits.index('mango'))