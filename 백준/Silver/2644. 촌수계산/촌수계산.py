import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
person_a, person_b = map(int, input().split())
m = int(input())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

def bfs(start):
    visited = [False] * (n+1)
    visited[start] = True
    q = deque([(start, 0)])
    while q:
        current, cnt = q.popleft()
        if current == person_b:
            return cnt
        for i in arr[current]:
            if visited[i] == False:
                visited[i] = True
                q.append((i, cnt + 1))
    return -1                

answer = bfs(person_a)  
print(answer)