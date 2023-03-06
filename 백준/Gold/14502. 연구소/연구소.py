def wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                wall(cnt+1)
                arr[i][j] = 0

def bfs():
    global maxv
    copy = [[0] * M for i in range(N)]
    for i in range(N):
        for j in range(M):
            copy[i][j] = arr[i][j]
    result = 0
    lst = []
    for i in range(N):
        for j in range(M):
            if copy[i][j] == 2:
                lst.append([i,j])
    while lst:
        a,b = lst[0][0], lst[0][1]
        del lst[0]
        for i in range(4):
            ax = a +dr[i]
            ay = b + dc[i]
            if 0 <= ax and 0 <= ay and ax < N and ay < M:
                if copy[ax][ay] == 0:
                    copy[ax][ay] = 2
                    lst.append([ax,ay])
    for i in copy:
        for j in i:
            if j == 0:
                result += 1
    maxv = max(maxv,result)

import sys

N, M = map(int,sys.stdin.readline().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
dr = [0,0,-1,1]
dc = [-1,1,0,0]
maxv = 0
wall(0)
print(maxv)