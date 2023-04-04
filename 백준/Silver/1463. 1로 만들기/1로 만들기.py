N = int(input())
q = [N]
visited = [0]*(N+1)
while q:
    c = q.pop(0)
    if c == 1:
        print(visited[1])
        break
    if not c % 3 and not visited[c//3]:
        q.append(c//3)
        visited[c//3] = visited[c] + 1
    if not c % 2 and not visited[c//2]:
        q.append(c//2)
        visited[c//2] = visited[c] + 1
    if not visited[c-1]:
        q.append(c-1)
        visited[c-1] = visited[c] + 1 
