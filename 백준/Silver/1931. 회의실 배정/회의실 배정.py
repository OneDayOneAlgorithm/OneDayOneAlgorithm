import sys
input = sys.stdin.readline

N = int(input())
lst = []
for i in range(N):
    a,b = map(int,input().split())
    lst.append((a,b))
lst.sort(key=lambda x:x[0])
lst.sort(key=lambda x:x[1])
end = lst[0][1]
cnt = 1
for i in range(1,N):
    if lst[i][0] >= end:
        end = lst[i][1]
        cnt += 1
print(cnt)