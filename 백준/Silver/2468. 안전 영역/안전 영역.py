import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

arr = []
for _ in range(N):
    row = list(map(int, input().split()))
    arr.append(row)

def bfs(node_r, node_c):
    visited = [[False] * N for _ in range(N)]
    visited[node_r][node_c] = True
    q = deque([(node_r, node_c)])
    while q:
        current_r, current_c = q.popleft()
        copy_arr[current_r][current_c] = 0
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_r, next_c = current_r + dr, current_c + dc
            if 0 <= next_r < N and 0 <= next_c < N and visited[next_r][next_c] == False and copy_arr[next_r][next_c] > 0:
                visited[next_r][next_c] = True
                q.append((next_r,next_c))
    return 0    

answer = 1
for rain in range(1, 101):
    total = 0
    copy_arr = [row[:] for row in arr]
    for i in range(N):
        for j in range(N):
            if copy_arr[i][j] <= rain:
                copy_arr[i][j] = 0              
    for i in range(N):
        for j in range(N):
            if copy_arr[i][j] > 0:
                bfs(i, j)
                total += 1  
                            
    if answer < total:
        answer = total

print(answer)