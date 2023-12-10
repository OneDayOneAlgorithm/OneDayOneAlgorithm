N = int(input())
board = [list(input()) for _ in range(N)]
test_board = [[0] * N for _ in range(N)]
test_board2 = [[0] * N for _ in range(N)]
cnt = 0
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
for i in range(N):
    for j in range(N):
        if not test_board[i][j]:
            cnt += 1
            q = [(i, j)]
            while q:
                cr, cc = q.pop(0)
                for dir in range(4):
                    nr = cr + dr[dir]
                    nc = cc + dc[dir]
                    if 0 <= nr < N and 0 <= nc < N and board[cr][cc] == board[nr][nc] and not test_board[nr][nc]:
                        test_board[nr][nc] = cnt
                        q.append((nr, nc))


for i in range(N):
    for j in range(N):
        if board[i][j] == 'G':
            board[i][j] = 'R'
cnt2 = 0
for i in range(N):
    for j in range(N):
        if not test_board2[i][j]:
            cnt2 += 1
            q = [(i, j)]
            while q:
                cr, cc = q.pop(0)
                for dir in range(4):
                    nr = cr + dr[dir]
                    nc = cc + dc[dir]
                    if 0 <= nr < N and 0 <= nc < N and board[cr][cc] == board[nr][nc] and not test_board2[nr][nc]:
                        test_board2[nr][nc] = cnt2
                        q.append((nr, nc))

print(cnt,cnt2)