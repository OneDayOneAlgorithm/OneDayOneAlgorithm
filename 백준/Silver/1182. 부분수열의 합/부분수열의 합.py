def solve(n,sum_v):
    global cnt
    if n == N:
        return
    if sum_v+arr[n] == S:
        cnt += 1
    solve(n+1,sum_v+arr[n])
    solve(n+1,sum_v)
N,S = map(int,input().split())
arr = list(map(int,input().split()))
cnt = 0
solve(0,0)
print(cnt)