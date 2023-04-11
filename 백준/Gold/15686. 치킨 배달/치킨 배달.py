import sys
from itertools import combinations
input = sys.stdin.readline

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
lst_1 = []
lst_2 = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            lst_2.append([i,j])
        if arr[i][j] == 1:
            lst_1.append([i,j])
ans = 99999
for i in combinations(lst_2,M):
    sm = 0
    for j in lst_1:
        min_v = 99999
        for k in i:
            d = abs(j[0]-k[0])+abs(j[1]-k[1])
            if min_v > d:
                min_v = d
        sm += min_v
    if ans > sm:
        ans = sm
print(ans)