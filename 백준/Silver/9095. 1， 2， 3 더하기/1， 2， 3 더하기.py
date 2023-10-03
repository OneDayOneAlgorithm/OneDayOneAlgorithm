# https://www.acmicpc.net/problem/9095
def n_sum(n):
    global cnt
    if n == 0:
        cnt += 1
        return
    if n < 0:
        return
    n_sum(n-1)
    n_sum(n-2)
    n_sum(n-3)
T = int(input())
for _ in range(T):
    n = int(input())
    cnt = 0
    n_sum(n)
    print(cnt)

