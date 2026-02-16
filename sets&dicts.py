info = {
    "name": "deelip", "marks": 24, "class": "7 th class"
}
print(info)


# Nested dictionary
info1 = {
    'name ': 'deelip',
    'marks': {
        'phy': 23,
        'chem': 29,
        'maths': 30
    }
}
print(info1['marks']['maths'])


# dictionary methods ( mutable , unsorted, donot allow duplicate keys )
'''
mydict.keys() returns all keys
mydict.values() returns all values
mydict.items() returns all(key,values) format pairs as turple
mydict.get("key") returns the valuees if not case returns None but in (mydict["key"])if
value not present it will returns error and rest of remanining cod will not excuted 
mydict.update(newdict)

'''
# set {}  ( allows unique values , immutable )
# for null set representation
a = {}  # this is dict
b = set()  # this is null set


# set methods
''' 
set.add(element) adds an element
set.remove(element)  removes the element 
set.clear()
set.pop()

'''
