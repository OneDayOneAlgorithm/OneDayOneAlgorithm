T = int(input()) #테스트케이스의 개수

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):           
    q = [(x,y)]
    board[x][y] = 0 # 방문처리

    while q:
        x,y = q.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue

            if board[nx][ny] == 1 :
                q.append((nx,ny))
                board[nx][ny] = 0

# 행렬만들기
for i in range(T):
    M, N, K = map(int,input().split())
    board = [[0]*(N) for _ in range(M)]
    cnt = 0
    for j in range(K):
        x,y = map(int, input().split())
        board[x][y] = 1
    for r in range(M):
        for c in range(N):
            if board[r][c] == 1:
                bfs(r,c)
                cnt += 1

    print(cnt)