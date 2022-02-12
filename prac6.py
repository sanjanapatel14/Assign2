#20CE102-SANJANA PATEL
#AIM: You are given n words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification. 
#GITHUB REPOSITARY LINK: https://github.com/sanjanapatel14/Assign2

#import counter
from collections import Counter
n=int(input ())
l=list()
for _ in range (n):
    l.append(input())
x=Counter(l)

print (len(x))
print(*x.values())