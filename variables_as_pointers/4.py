dict1 = {
    'a': [1, 2, 3],
    'b': (4, 5, 6),
}

dict2 = dict(dict1)
dict1['a'][1] = 42
print(dict2['a'])

# this code will print: [1, 42, 3]. In this case we are creating a 
# shallow copy of dict1 and assigning it to the variable dict2. 
# Shallow copies share nested elements ie. they point to the same 
# objects. Therefore any change made to the nested list [1, 2, 3] 
# in dict1 will be reflected in dict2