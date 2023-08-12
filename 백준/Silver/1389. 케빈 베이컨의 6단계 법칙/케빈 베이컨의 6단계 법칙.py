from collections import deque

def BFS(N, start):
    visit = [start]
    count = [0] * (N + 1)
    q = deque()
    q.append(start)
    while q:
        c = q.popleft()
        for i in graph[c]:
            if i not in visit:
                q.append(i)
                visit.append(i)
                count[i] = count[c] + 1
    return sum(count)



N, M = map(int, input().split())
graph = [[] for i in range(N + 1)]
result = []
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, N + 1):
    result.append(BFS(N, i))
print(result.index(min(result)) + 1)