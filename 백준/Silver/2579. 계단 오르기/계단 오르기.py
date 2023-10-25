# https://www.acmicpc.net/problem/2579
import sys

input = sys.stdin.readline
N = int(input())
lst = [0] * 301
for i in range(1,N+1):
    lst[i] = int(input())
total = [0] * 301
total[1] = lst[1]
total[2] = lst[1] + lst[2]
total[3] = max(lst[1] + lst[3], lst[2] + lst[3])
for i in range(4,N+1):
    total[i] = max(total[i-3] + lst[i-1] + lst[i], total[i-2] + lst[i])
print(total[N])

