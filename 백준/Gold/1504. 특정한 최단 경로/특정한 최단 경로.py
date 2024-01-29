import sys
input = sys.stdin.readline

def dijkstra(n):
    visited = [1e9] * (N+1)
    visited[n] = 0
    q = [(n,0)]
    while q:
        current, distance = q.pop(0)
        for i in graph[current]:
            if visited[i[0]] < distance+i[1]:
                continue
            else:
                visited[i[0]] = distance+i[1]
                q.append((i[0],distance+i[1]))
    return visited
    
    

N,E = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
v1,v2 = map(int,input().split())
value_1 = dijkstra(1)
value_v1 = dijkstra(v1)
value_v2 = dijkstra(v2)
result = min(value_1[v1] + value_v1[v2] + value_v2[N],value_1[v2] + value_v2[v1] + value_v1[N])
if result >= 1e9:
    print(-1)
else:
    print(result)
