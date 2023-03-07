thisDict = {"brand": "Ford", "model": "mustang", "year": 1990, "year": 1900}
print(thisDict)
print(len(thisDict))

thisDict = {"brand": "ford", "electric": False, "year": 1964, "colors": ['red', 'white', 'blue']}
print(thisDict['colors'])
print(type(thisDict))

print(thisDict.get('colors'))
# get all dictionary keys
all_dict_key = thisDict.keys()
print(all_dict_key)

# get values of dictinary

# Add value in dict
thisDict["owner"] = 'American'
print(thisDict)

thisDict["want_to_sell"] = True
all_value_dict = thisDict.values()
print(all_value_dict)



for x in thisDict:
    print(thisDict[x])

if 'model' in thisDict:
    print("yes, model is the key of this dictionary")

print('----------------dict Methods--------------')
# Changes Dictionary

thisDict = {"brand": "Ford",
            "model": "mustang",
            "electric": False,
            "colors": ['red', 'white', 'blue'],
            "year": 1990}

thisDict["year"] = 1992
print(thisDict)

thisDict.update({'model': 'corola'})
print(thisDict)

# Add item
thisDict['owner'] = True
print(thisDict)

thisDict.update({'want_to_sell': True})
print(thisDict)


print('-----------Remove Item from Dict----------')
thisDict = {"brand": "Ford",
            "model": "mustang",
            "electric": False,
            "colors": ['red', 'white', 'blue'],
            "year": 1990}

thisDict.pop('model')
print(thisDict)

thisDict.popitem()
print(thisDict)

del thisDict['brand']
print(thisDict)

thisDict.clear()
print(thisDict)

del thisDict

print('------------Loop through Dictionary---------')
thisDict = {"brand": "Ford",
            "model": "mustang",
            "electric": False,
            "colors": ['red', 'white', 'blue'],
            "year": 1990}

for x in thisDict:
    print(x)
    print(thisDict[x])
print('------------')
for x in thisDict.values():
    print(x)

for x in thisDict.keys():
    print(x)

print("----------Get both key & value in loop-----------")
thisDict = {"brand": "Ford",
            "model": "mustang",
            "electric": False,
            "colors": ['red', 'white', 'blue'],
            "year": 1990}

for x, y in thisDict.items():
    print("Key: "+ str(x) +" :Value: " + str(y))


print("----------Dictionary Copy-----------")
thisDict = {"brand": "Ford",
            "model": "mustang",
            "electric": False,
            "colors": ['red', 'white', 'blue'],
            "year": 1990}

myDict = thisDict.copy()
print(myDict)

mydict2 = dict(thisDict)
print(mydict2)

print("------Nested dictionary-------")
family_dict = {
    'child1': {
        'name': 'Emil',
        'year': 2004
    },
    'child2':{
        'name': 'tobias',
        'year': 2007
    },
    'child3': {
        'name': 'Linus',
        'year': 2011
    }
}

print(family_dict['child1'])

family_dict['child1']


child1 = {
    'name': 'Emily',
    'year': 2006
}
chiild2 = {
    'name': 'Tobia',
    'year': 2007
}
child3 = {
    'name': 'Linus',
    'year': 2011
}

my_family = {
    'child1': child1,
    'child2': chiild2,
    'child3': child3
}
#print(my_family['child1'])

for x in my_family.keys():
    print(x)

my_family_2 = dict(my_family)
print(my_family_2)


for x in my_family.items():
    print(x)


my_family_2 = family_dict.copy()
print(my_family_2)

my_family_2 = dict.fromkeys(('key1','key2','key3'), 3)
print(my_family_2)

my_family_2 = dict(my_family)
print(my_family_2)

print(my_family.get('child1'))

print(type(my_family.items()))

print(my_family.items())

print(my_family.keys())

my_family.pop('child1')
print(my_family)

my_family.popitem()
print(my_family)

my_family.setdefault('child1', {'name': 'Emily', 'year': 2006})
print(my_family)
print(my_family.setdefault('child1'))

my_family.update({'child4': {'name': 'nasir', 'year': 2022}})

my_family.update({'child5': False})
my_family.update({'child5': True})
print(my_family)
"""
my_family.clear()
print(my_family)
"""

x = dict.fromkeys(my_family.keys(), 3)
print(x)


if 'child1' in my_family:
    print("yes")