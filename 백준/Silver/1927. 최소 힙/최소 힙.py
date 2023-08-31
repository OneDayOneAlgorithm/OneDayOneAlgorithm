# https://www.acmicpc.net/problem/1927
import sys
import heapq
N = int(input())
heap = []
for _ in range(N):
    num = int(sys.stdin.readline())
    if not num:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)
    else:
        heapq.heappush(heap, num)