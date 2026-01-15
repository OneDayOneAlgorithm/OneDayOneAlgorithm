import sys
from collections import deque

input = sys.stdin.readline
K = int(input())

def bfs(node):
    q = deque([node])
    visited[node] = 0
    while q:
        c = q.popleft()
        #print('c =', c)
        for nc in arr[c]:
            if 1 <= nc <= V:
                #print('nc =', nc)
                if visited[nc] == -1:
                    visited[nc] = visited[c] + 1
                    q.append(nc)
                    #print('YES')
                elif visited[nc] == visited[c] - 1 or visited[nc] == visited[c] + 1:
                    #print('continue')
                    continue 
                else:
                    #print('NO')
                    return False
    return True

for _ in range(K):
    V, E = map(int, input().split())
    pass_yn = True
    arr = [[] for _ in range(V + 1)]
    visited = [-1] * (V + 1)
    for _ in range(E):
        u, v = map(int, input().split())
        arr[u].append(v)
        arr[v].append(u)
    for i in range(1, V + 1):
        if visited[i] == -1:
            pass_yn = bfs(i)        
        if pass_yn == False:
            print('NO')
            break
    else:
        print('YES')