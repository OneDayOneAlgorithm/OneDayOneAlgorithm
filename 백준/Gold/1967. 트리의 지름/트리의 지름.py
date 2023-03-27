import sys
sys.setrecursionlimit(10**9)
def DFS(n,distance):
    for (a,b) in tree[n]:
        if visited[a] == 0:
            visited[a] = distance + b
            DFS(a, distance + b)

N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b,c = map(int,input().split())
    tree[a].append([b,c])
    tree[b].append([a,c])
visited = [0] * (N+1)
visited[1] = 1
DFS(1,1)

end = visited.index(max(visited))
visited = [0]*(N+1)
visited[end] = 1
DFS(end,1)
print(max(visited)-1)