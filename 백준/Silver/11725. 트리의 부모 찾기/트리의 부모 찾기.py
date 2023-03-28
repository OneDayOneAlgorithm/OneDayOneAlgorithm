def bfs():
    while q:
        c = q.pop(0)        # 현재 노드번호를 팝해서 c에 넣는다.
        for i in graph[c]:  # 현재 노드번호의 자식일 수 있는 것들을 순환한다.
            if not ans[i]:  # ans에서 0일시 그 노드는 자식임이 확정되고
                ans[i] = c  # ans에 부모인 c를 넣는다.
                q.append(i)  # 그 노드를 부모로 쓰기위해 q에 넣는다.


N = int(input())
graph = [[] for _ in range(N+1)]    # 0행부터 N행까지의 그래프를 만든다. (0행은 안 쓴다.)
for _ in range(N-1):  # 그래프에 두 노드씩 입력한다.
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
ans = [0] * (N+1)    # N+1개의 크기를 갖는 ans를 만든다. (0번째 원소는 사용하지 않는다.)
q = [1]              # 1번 노드부터 시작하기 위해 q에 1을 넣는다.
bfs()                # bfs 함수를 시작한다.
for i in ans[2:]:    # 2번노드의 부모부터 출력한다.
    print(i)
