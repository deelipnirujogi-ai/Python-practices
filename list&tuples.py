a = [3.4, "dileep", 5, True]
print(a)
print(a[3])
a.pop(True)
print(a)
# slicing possible in the lists
print(a[0:])
print(a[::-1])
print((a))


# lists methods
''' list.append(1)
list.sort()  arranging in the ascending order
list.sort(reverse=True) arranging in the descending order
list.reverse() just reversing the list
list.insert(index,element)
list.pop(index)
list.insert(index)
'''
list = [1, 2, 3, 323, 2, 3, 1]
newone = list.sort()
print(list)
print(sorted(list))
# .sort() always returns the None as deflaut


#   tupules  represented with ()  immutable and string also immutable
tup = (1)  # it will consider as normal value so it not a tuple
tup1 = (1.2)
tup2 = ('strinnng')
tup4 = (2,)  # for the single element , is important
print(type(tup))
print(type(tup1))
print(type(tup2))
print(type(tup4))


lis1 = [1, 2, 3, 2323, 232, 2]
lis1.count(2)
print(lis1)
