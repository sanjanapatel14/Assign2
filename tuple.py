#20CE102
#SANJANA PATEL
# 1 Write a Python program to create a tuple with different data types.

tpl = ("tuple",1000,True,1.08)
print(type(tpl))
print(tpl)


# 2 Write a Python program to create a tuple with numbers and print one item.

tpl = (1,2,3,4,5,6,7,8,9,10)
print(tpl[0])
print(tpl[5])

# 3 Write a Python program to add an item in a tuple.

a=(13,12,47,56)
print(a)
b=list(a)
print(b)
b.append(10)
print(b)
c=tuple(b)
print(c)


# 4 Write a Python program to convert a tuple to a string.

tpl = ('S', 'A', 'N', 'J', 'A', 'N', 'A', ' ', 'P', 'A', 'T', 'E','L')
str = ''.join(tpl)
print(str)

# 5 Write a Python program to find the length of a tuple.

tpl = ('P', 'A', 'T', 'E','L')
print(tpl)
print(len(tpl))