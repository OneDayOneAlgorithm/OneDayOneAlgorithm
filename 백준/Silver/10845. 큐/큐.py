import sys
input = sys.stdin.readline
N = int(input())
q = []
for i in range(N):
    arr = list(input().split())
    if arr[0] == 'push':
        q.append(int(arr[1]))
    elif arr[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif arr[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)
    elif arr[0] == 'size':
        print(len(q))
    elif arr[0] == 'empty':
        if len(q):
            print(0)
        else:
            print(1)
    else:
        if q:
            print(q.pop(0))
        else:
            print(-1)