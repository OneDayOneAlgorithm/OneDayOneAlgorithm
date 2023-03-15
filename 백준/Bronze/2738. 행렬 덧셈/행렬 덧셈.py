N,M = map(int,input().split())
lst = []
for i in range(N):
    lst += list(map(int,input().split()))
lst2 = []
for i in range(N):
    lst2 += list(map(int,input().split()))
lst3 = []
for i in range(M*N):
    lst3.append(lst[i] + lst2[i])

lst4 = []
for i in range(0,N*M,M):
    lst4.append(lst3[i:i+M])
for i in range(N):
    print(*lst4[i])