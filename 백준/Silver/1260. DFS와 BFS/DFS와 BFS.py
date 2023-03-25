from collections import deque
import sys
# 재귀 제한에 걸리므로 제한을 풀어줘야 한다.
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n,m,v = map(int,input().split())
l = [list(map(int,input().split())) for i in range(m)]

# 정점의 번호를 인덱스로 그대로 사용하기 위해 한 개 만큼 크게 만들어주었다.
graph = [[0 for i in range(n+1)] for i in range(n+1)]
d_visit = []
b_visit = []

deq = deque()

# 인접 행렬로 그래프를 표현
for i,j in l:
    graph[i][j] = 1
    graph[j][i] = 1

def dfs(v):
    if v not in d_visit:
        d_visit.append(v)
    else:
        return
    
    for i in range(1,n+1):
        if graph[v][i]:
            dfs(i)
            
def bfs(v):
    if v not in b_visit:
        b_visit.append(v)
        
    for i in range(1,n+1):
        if graph[v][i] and i not in b_visit:
            deq.append(i)
            b_visit.append(i)
            
    if deq:
        bfs(deq.popleft())

dfs(v)
bfs(v)
print(*d_visit)
print(*b_visit)

