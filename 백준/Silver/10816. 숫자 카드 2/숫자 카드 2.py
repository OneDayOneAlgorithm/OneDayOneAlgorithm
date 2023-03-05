M = int(input())
c_card = list(map(int,input().split()))
N = int(input())
arr = list(map(int,input().split()))
lst = [0]*20000001
for i in c_card:
    lst[i+10000000] += 1
for i in arr:
    print(lst[i+10000000],end=' ')