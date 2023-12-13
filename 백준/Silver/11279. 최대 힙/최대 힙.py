import sys
import heapq as hq

input = sys.stdin.readline
N = int(input())
lst = []
for _ in range(N):
    x = int(input())
    if x == 0:
        if not lst:
            print(0)
        else:
            print(hq.heappop(lst)[1])
    else:
        hq.heappush(lst,(-x,x))