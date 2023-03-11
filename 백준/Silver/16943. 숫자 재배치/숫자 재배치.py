def solve(n):
    if len(n) == len(A):
        if int(n) < B and n[0] != '0':
            lst.append(int(n))
            return
        else:
            return
    for i in range(len(A)):
        if used[i] == 0:
            used[i] = 1
            solve(n+A[i])
            used[i] = 0

A,B = map(int,input().split())
A = str(A)
used = [0]*len(A)
lst = []
solve('')
if lst:
    print(max(lst))
else:
    print(-1)
