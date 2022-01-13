#20CE102 SANJANA PATEL
####### 1 Write a Python program to add member(s) in a set and clear a set

set={'Sanjana',102,'Patel','python'}
print(set)
set.add('python lab') # for adding single element
print(set)
set.update(['course id 259','Learn with fun '])
print(set)
a=set.clear()
print(a)

####### 2  Write a Python program to remove an item from a set if it is present in the set.

set={1,2,3,4,5,6,7,8,9,10,'Sanjana','Patel'}
print(set)
# #removing 10 from set
set.remove(10)
print(set)
set.remove('Patel')
print(set)

####### 3 Write a Python program to create an intersection, Union, difference of sets.

a = {1,2,4,6,10,100,120}
b = {1,34,44,98,65,98,45}
c = {2,34,45,9,10}

print("A U B = ", a.union(b))
print("A ∩ B = ", a.intersection(b))
print("A - B = ", a.difference(b))

####### 4 Write a Python program to find maximum and the minimum value in a set.

set = {12,55,5,22,10,23}
print(set)
print("Maximum value :",max(set))
print("Minimum value :",min(set))