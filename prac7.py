#20CE102-SANJANA PATEL
#Lapindrome is defined as a string which when split in the middle, gives two halves having the same characters and same frequency of each character. If there are odd number of characters in the string, we ignore the middle character and check for lapindrome. For example gaga is a lapindrome, since the two halves ga and ga have the same characters with same frequency. Also, abccab, rotor and xyzxy are a few examples of lapindromes. Note that abbaab is NOT a lapindrome. The two halves contain the same characters but their frequencies do not match. Your task is simple. Given a string, you need to tell if it is a lapindrome. 
#GITHUB REPOSITARY LINK: https://github.com/sanjanapatel14/Assign2

T = int(input())
for i in range(T):
    n = input()
    l = len(n)
    b,c="",""
    if l % 2 == 0:
        b=n[:l//2]
        c = n[l//2:]  
    else:
        b=n[:l//2]
        c = n[l//2+1:]
    l1=list(b)
    l2=list(c)
    l1.sort()
    l2.sort()
    b=str(l1)
    c=str(l2)        
    if (b==c):
        print("YES")
    else:
        print("NO")