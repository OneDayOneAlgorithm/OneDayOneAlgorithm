import sys
input = sys.stdin.readline

def func(n):
    q = []
    distance = [99999] * (N+1)
    q.append((0,n))
    distance[n] = 0
    while q:
        d,c = q.pop(0)
        if distance[c] < d:
            continue
        for j in graph[c]:
            sm = d + j[1]
            if distance[j[0]] > sm:
                distance[j[0]] = sm
                q.append((sm, j[0]))
    return distance


N, M, X = map(int,input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int,input().split())
    graph[a].append((b,c))
# print(graph)

# print(distance_x)

result = 0
for i in range(1,N+1):
    go = func(i)
    back = func(X)
    result = max(result, go[X]+back[i])

print(result)

# distance를 list로 만들어서 INF 넣어두기
# func 시작해서 distance[i] = 0 만들고 모든 경우의수 다돌아서 distance만들기 이때 distance[i]<d 가되면 return 시켜서버리기
# distance[X] 값 꺼내오고 distance INF로 초기화
# func을 X에서 시작 후 위 2번 문항을 반복하여 distance[i] 값 꺼내오기
# 두 값을 더하고 이 값을 result에 할당. 이후 max(result, 두 값의 합) 출력