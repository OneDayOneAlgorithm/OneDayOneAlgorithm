import sys
input = sys.stdin.readline
N = int(input())
q = []
for i in range(N):
    arr = input().split()
    if arr[0] == 'push_front':
        q.insert(0,int(arr[1]))
    elif arr[0] == 'push_back':
        q.append(int(arr[1]))
    elif arr[0] == 'pop_front':
        if q:
            print(q.pop(0))
        else:
            print(-1)
    elif arr[0] == 'pop_back':
        if q:
            print(q.pop())
        else:
            print(-1)
    elif arr[0] == 'size':
        print(len(q))
    elif arr[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
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
