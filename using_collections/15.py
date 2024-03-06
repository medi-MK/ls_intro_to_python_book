pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

keys = pets.keys()
del pets['Dog']
pets['Snake'] = 'Sssss'
print(keys)

# The `keys` varable is assigned the value of a **dictionary viewing object**
# it will update immediately as the original dictionary `pets` is updated

# ['Cat', 'Bird', 'Snake']