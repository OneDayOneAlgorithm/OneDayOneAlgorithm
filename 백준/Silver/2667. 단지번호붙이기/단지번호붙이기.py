N = int(input())
map = [list(map(int,str(input()))) for _ in range(N)]
q = []
dr = [1,-1,0,0]
dc = [0,0,1,-1]
total = 0
lst = []
for i in range(N):
    for j in range(N):
        if map[i][j] == 1:
            map[i][j] = 0
            cnt = 1
            q.append((i,j))
            while q:
                cr,cc = q.pop(0)
                for dir in range(4):
                    nr, nc = cr + dr[dir], cc + dc[dir]
                    if 0<=nr<N and 0<=nc<N and map[nr][nc]==1:
                        q.append((nr,nc))
                        map[nr][nc] = 0
                        cnt += 1
            total += 1
            lst.append(cnt)
print(total)
lst.sort()
for i in lst:
    print(i)
                        