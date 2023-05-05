def dfs(start, depth):
    # 해당 노드를 방문 체크 한다.
    visited[start] = 1
    # 해당 시작점을 기준으로 계속해서 dfs로 그래프를 탐색한다.
    for i in graph[start]:
        # 해당 노드와 연결된 노드가 방문하지 않았던 노드라면
        if not visited[i]:
            dfs(i, depth+1)


N,M = map(int,input().split())
# 정점 개수 + 1개의 그래프를 만든다.
graph = [[] for _ in range(N+1)]
# 정점 개수 + 1개의 방문지점을 만든다.
visited = [0]*(N+1)
# 간선의 양 끝점을 받는다.
for i in range(M):
    a,b = map(int,input().split())
    # 양방향이므로 서로 저장한다.
    graph[a].append(b)
    graph[b].append(a)
cnt = 0
# 1번노드부터 마지막 노드까지 순회
for i in range(1,N+1):
    if not visited[i]:
        if not graph[i]:
            cnt += 1
            visited[i] = 1
        else:
            dfs(i,0)
            cnt += 1
print(cnt)



