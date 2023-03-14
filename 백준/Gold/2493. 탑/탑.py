import sys

input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
stack = []
ans = [0] * N  # N개의 정답 배열
for i in range(N):
    if stack:  # 스택에 원소가 있으면
        while stack and arr[i] > arr[stack[-1]]:  # 현재 인덱스에 해당하는 원소와 스택 맨 뒤에 있는 원소를 비교해서 스택의 원소가 작으면
            stack.pop()  # 스택의 맨 뒤에 있는 원소를 제거한다.
        if stack:   # 스택에 원소가 있으면
            ans[i] = stack[-1]+1    # 스택 맨 뒤에 있는 원소에 1을 더해서 답에 기록한다.
        stack.append(i) # 그리고 현재 원소를 stack에 추가한다.
    else:   # 스택에 원소가 없으면
        stack.append(i) # 그냥 스택에 현재 인덱스에 해당하는 원소를 추가한다.
print(*ans)
