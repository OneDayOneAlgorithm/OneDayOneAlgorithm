import sys
import heapq

input = sys.stdin.readline
V, E = map(int,input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    a, b, c = map(int,input().split())
    graph[a].append((b,c))
INF = sys.maxsize
distance = [INF]*(V+1)
q = []
heapq.heappush(q,(0,K)) # [(0,1)]
distance[K] = 0
while q:
    current = heapq.heappop(q) # [(0,1)]
    if current[0] > distance[current[1]]: # 1 vs INF
        continue
    
    for i in graph[current[1]]: # i == (2,2), (3,3)
        next_distance = i[1] + current[0] # 2 + 1
        if next_distance > distance[i[0]]: # 3 > INF
            continue
        distance[i[0]] = next_distance
        heapq.heappush(q,(next_distance,i[0]))
for i in distance[1:]:
    if i == INF:
        print("INF")
        continue
    print(i)
