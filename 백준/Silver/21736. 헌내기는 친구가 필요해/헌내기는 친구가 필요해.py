N, M = map(int,input().split())
board = [list(input()) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
dr = [1,-1,0,0]
dc = [0,0,-1,1]
stop = 0
cnt = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 'I':
            q = [(i,j)]
            stop = 1
            break
    if stop:
        break
while q:
    cr,cc = q.pop(0)
    for dir in range(4):
        nr, nc = cr + dr[dir], cc + dc[dir]
        if 0 <= nc < M and 0 <= nr < N and not visited[nr][nc] and board[nr][nc] != 'X':
            visited[nr][nc] = 1
            q.append((nr,nc))
            if board[nr][nc] == 'P':
                cnt += 1
if not cnt:
    print('TT')
else:
    print(cnt)

