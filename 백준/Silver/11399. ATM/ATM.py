# https://www.acmicpc.net/problem/11399
def func(cnt, sm):
    global total
    total += sm
    if cnt == N-1:
        return
    func(cnt+1, sm+P[cnt+1])
    return

N = int(input())
P = list(map(int, input().split()))
total = 0
P.sort()
func(0, P[0])
print(total)
