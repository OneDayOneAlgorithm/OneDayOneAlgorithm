import sys
input = sys.stdin.readline
def solve(B):
    c = 0
    min_vv = 9999999
    while c<=256:
        block = B
        cnt = 0
        for i in range(N):
            for j in range(M):
                if c > ground[i][j]:
                    cnt += (c - ground[i][j])
                    block -= (c - ground[i][j])
                else:
                    cnt += (ground[i][j] - c)*2
                    block += (ground[i][j] - c)
        if block >= 0:
            min_vv = cnt
            lst.append((cnt,c))
        c += 1

N,M,B = map(int,input().split())
ground = [list(map(int,input().split())) for _ in range(N)]
lst = []
solve(B)
lst.sort(key=lambda x:x[1], reverse=True)
lst.sort(key=lambda x:x[0])
print(*lst[0])



