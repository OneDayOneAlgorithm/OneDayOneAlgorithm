import sys
input = sys.stdin.readline
def solve(r,c,cnt):
    global ans
    used[ord(map[r][c])-65] = 1
    for nr,nc in ((r+1,c),(r-1,c),(r,c+1),(r,c-1)):
        if 0<=nr<R and 0<=nc<C and not used[ord(map[nr][nc])-65]:
            used[ord(map[nr][nc])-65] = 1
            solve(nr,nc,cnt+1)
            used[ord(map[nr][nc])-65] = 0
    if ans < cnt:
        ans = cnt

R,C = map(int,input().split())
map = [list(input()) for _ in range(R)]
used = [0]*26
ans = 0
solve(0,0,1)
print(ans)