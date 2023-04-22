from collections import deque

N,K = map(int,input().split())
q = deque()
q.append(N)
visited = [0] * (10**5+1)
visited[N] = 1
while q:
    value = q.popleft()
    if value == K:
        print(visited[value]-1)
        break
    for i in (value+1,value-1,value*2):
        if 0<=i<=10**5 and not visited[i]:
            q.append(i)
            visited[i] += visited[value]+1
