N = int(input())
stack = []
arr = [int(input()) for _ in range(N)]
for i in range(N):
    if arr[i]:
        stack.append(arr[i])
    else:
        stack.pop()
print(sum(stack))