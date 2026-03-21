import sys

input = sys.stdin.readline

N = int(input())

for i in range(1, N + 1):
    mx = i * 2 - 1
    print(' ' * (N - i) + '*' * mx)

for i in range(N - 1, 0, -1):
    mx = i * 2 - 1
    print(' ' * (N - i) + '*' * mx)