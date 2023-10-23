# https://www.acmicpc.net/problem/2178
N,M = map(int,input().split())
board = [list(map(int,list(input()))) for _ in range(N)]
board_cnt = [[0]*M for _ in range(N)]
dr = [0,0,1,-1]
dc = [1,-1,0,0]
q = []
q.append((0,0))
board_cnt[0][0] = 1
while q:
    cr,cc = q.pop(0)
    for dir in range(4):
        nr,nc = cr+dr[dir], cc+dc[dir]
        if 0<=nr<N and 0<=nc<M and board[nr][nc] == 1 and not board_cnt[nr][nc]:
            q.append((nr,nc))
            board_cnt[nr][nc] = board_cnt[cr][cc] + 1
print(board_cnt[N-1][M-1])