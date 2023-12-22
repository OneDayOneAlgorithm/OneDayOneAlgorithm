N,M = map(int,input().split())
note = {}
for _ in range(N):
    address, password = input().split()
    note[address] = password
for _ in range(M):
    address = input()
    print(note[address])