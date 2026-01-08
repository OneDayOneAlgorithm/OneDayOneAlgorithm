import sys
from collections import deque

input = sys.stdin.readline
M, N, K = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(K)]
arr = [[0] * N for _ in range(M)]
for i in range(K):
    row_minus = lst[i][3] - lst[i][1] # 4
    culumn_minus = lst[i][2] - lst[i][0] # 2
    start_row = lst[i][1] # 0
    start_column = lst[i][0] # 2
    for j in range(row_minus):
        for k in range(culumn_minus):
            arr[start_row + j][start_column + k] = True    

def bfs(i, j):
    q = deque([(i, j)])
    arr[i][j] = 1
    tmp = 0
    while q:
        tmp += 1
        cr, cc = q.popleft()
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < M and 0<= nc < N and arr[nr][nc] == False:
                q.append((nr, nc))
                arr[nr][nc] = True                            
    return tmp

cnt = 0
result = [] 
for i in range(M):
    for j in range(N):
        if arr[i][j] == False:            
            result.append(bfs(i, j))
            cnt += 1    
result.sort()               

print(cnt)
print(*result)