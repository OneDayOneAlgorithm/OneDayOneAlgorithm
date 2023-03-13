import sys
# from collections import deque
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    p = str(input().rstrip())
    N = int(input())
    arr = input().rstrip()[1:-1].split(',')
    q = []
    for i in range(N):
        q.append(arr[i])
    status = 1
    flag = 1
    for i in p:
        if i == 'R':
            if status == 1:
                status = -1
            else:
                status = 1
        elif i == 'D':
            if q:
                if status == 1:
                    q.pop(0)
                else:
                    q.pop()
            else:
                print('error')
                flag = 0
                break
    if flag:
        if status == 1:
            print("[", end="")
            print(*q, sep=",", end="")
            print("]")
        else:
            q.reverse()
            print("[", end="")
            print(*q, sep=",", end="")
            print("]")
