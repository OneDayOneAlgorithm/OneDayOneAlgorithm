# https://www.acmicpc.net/problem/1764
N, M = map(int,input().split())
lst = set()
lst2 = set()
for i in range(N):
    lst.add(input())
for i in range(M):
    lst2.add(input())
result = sorted(list((lst & lst2)))
print(len(result))
for i in result:
    print(i)

