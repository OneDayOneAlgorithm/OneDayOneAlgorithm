import sys
input = sys.stdin.readline
N,M = map(int,input().strip().split())
note = {}
for _ in range(N):
    address, password = input().strip().split()
    note[address] = password
for _ in range(M):
    address = input().strip()
    print(note[address])