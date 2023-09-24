# https://www.acmicpc.net/problem/2630
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
cnt_0 = 0
cnt_1 = 0
def cut(r, c, N):
    global cnt_0, cnt_1
    num = board[r][c]
    for i in range(r,r+N):
        for j in range(c,c+N):
            if num != board[i][j]:
                cut(r, c, N//2)
                cut(r + N//2, c, N//2)
                cut(r, c + N//2, N//2)
                cut(r + N//2, c + N//2, N//2)
                return
    if num == 0:
        cnt_0 += 1
    else:
        cnt_1 += 1
cut(0, 0, N)
print(cnt_0)
print(cnt_1)