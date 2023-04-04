def dfs(x,y,z):
    global cnt
    if x == N - 1 and y == N-1:
        cnt +=1
        return
    if x<N-1 and y<N-1:
        if map[x+1][y+1] == 0 and map[x][y+1] == 0 and map[x+1][y] == 0:
            dfs(x+1,y+1,2)
    if z==0 or z==2:
        if y<N-1:
            if map[x][y+1] == 0:
                dfs(x,y+1,0)
    if z==1 or z==2:
        if x<N-1:
            if map[x+1][y] == 0:
                dfs(x+1,y,1)

N = int(input())
map = [list(map(int,input().split())) for _ in range(N)]
cnt = 0
dfs(0,1,0)
print(cnt)