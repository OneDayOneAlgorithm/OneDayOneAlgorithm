N = int(input())
stack = []
arr = [list(input().split()) for _ in range(N)]
for i in range(N):
    if arr[i][0] == 'push':
        stack.append(int(arr[i][1]))
    elif arr[i][0] == 'top':
        if not stack:
            print('-1')
        else:
            print(stack[-1])
    elif arr[i][0] == 'size':
        print(len(stack))
    elif arr[i][0] == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif arr[i][0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
