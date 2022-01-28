#20CE102-SANJANA PATEL

n=int(input())  # taking input for n
arr=map(int,input().split())  # input for runner-ups
print("The runner-up score :",sorted(list(set(arr)))[-2])  # sorting the list