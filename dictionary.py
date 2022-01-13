#20CE102
#SANJANA PATEL
# 1.Add New Dictionary
def check(a):
    if a in emp:
         print("We found the key")
    else:
         print("Entered key not available")

emp ={
     1: 102,
     2: 'Sanjana',
     3: 'GET key 1',
     4: 'get key 2'
}
b = int(input("Enter any key name:"))
check(b)

if "id" in emp :
    print("We found the key")
else :
    print("Entered key not available")
a = input(("Enter key name : "))

# 2.Merge
emp1 = {'name_1' : 'Sanjana','age_1' : 20,'salary_1' : 100000}
emp2 = {'name_2' : 'Hetvi','age_2' : 20,'salary_2' : 18000}

print("First Dictionary :",emp1)
print("Second Dictionary :",emp2)
print("Merging first and second Dictionary ",emp1,emp2)

##3 sum
dict = {
     'a' : 100,
     'b' : 199,
     'c' : 122
}
sum = 0
for i in dict.values() : sum = sum +i
print("Sum of values",sum)

#Write a Python script to add a key to a dictionary.
d = {0:10, 1:20}
print(d)
d.update({2:30})
print(d)

#Write a Python script to concatenate following dictionaries to create a new one.
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3): dic4.update(d)
print(dic4)