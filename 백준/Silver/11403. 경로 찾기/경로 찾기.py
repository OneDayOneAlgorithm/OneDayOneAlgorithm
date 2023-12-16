N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
mark = [[0]*N for _ in range(N)]

def func(s,i):
    for j in range(N):
        if board[i][j] and not visit[j]:
            visit[j] = 1
            mark[s][j] = 1
            func(s,j)

for i in range(N):
    visit = [0] * N
    func(i,i)

for result in mark:
    print(*result)
