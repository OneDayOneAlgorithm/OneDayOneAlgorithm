# https://www.acmicpc.net/problem/2606
N = int(input())
couple = int(input())
lst = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(couple):
    a,b = map(int,input().split())
    lst[a].append(b)
    lst[b].append(a)
visited[1] = 1
cnt = 0
q = [1]
while q:
    c = q.pop(0)
    for j in lst[c]:
        if not visited[j]:
            visited[j] = 1
            q.append(j)
            cnt += 1
print(cnt)