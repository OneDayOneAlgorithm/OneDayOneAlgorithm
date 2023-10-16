# https://www.acmicpc.net/problem/11659
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst2 = [0] * (N+1)
for i in range(N):
    lst2[i+1] = lst[i] + lst2[i]
for _ in range(M):
    i, j = map(int, input().split())
    print(lst2[j] - lst2[i-1])
