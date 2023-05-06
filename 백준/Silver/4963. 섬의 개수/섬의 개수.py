while True:
    w,h = map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    cnt = 0
    if not board or not w or not h:
        break
    dr = [0,0,-1,-1,-1,1,1,1]
    dc = [-1,1,-1,0,1,-1,0,1]
    for i in range(h):
        for j in range(w):
            if board[i][j] and not visited[i][j]:
                cnt += 1
                q=[(i,j)]
                while q:
                    cr, cc = q.pop(0)
                    for dir in range(8):
                        nr = cr + dr[dir]
                        nc = cc + dc[dir]
                        if 0<=nr<h and 0<=nc<w and board[nr][nc] and not visited[nr][nc]:
                            q.append((nr,nc))
                            visited[nr][nc] = 1
    print(cnt)
