N = int(input())
num = []            # 입력한 수열
for i in range(N):
    num.append(int(input()))
ans = []            # + 또는 - 배열
stack = [1]         # 1~N
ans.append('+')     # 처음에 ans에 + 러스를 넣고 stack에 1을 넣는다
i = 2               # stack에 1을 넣엇으니 2부터 시작
NO = False
while num:          # num가 있을 동안 계속 반복
    if not stack:
        stack.append(i)
        ans.append('+')
        i += 1
    elif stack[-1] < num[0]:          # stack 마지막 값보다 num[0]이 크면
        while stack[-1] < num[0]:   # 같이 질때 까지 stack에 값을 넣는다
            stack.append(i)
            ans.append('+')         # 동시에 ansdp + 추가
            i += 1                  # i 도 계속 증가
        stack.pop(-1)               # 같아지면 stack마지막 값을 지우고
        ans.append('-')             # ans 에 - 추가하고
        num.pop(0)                  # num의 첫번째값을 지운다
    elif stack[-1] == num[0]:         # stack 마지막값과 num[0]이 같으면
        stack.pop(-1)               # 같아지면 stack마지막 값을 지우고
        ans.append('-')             # ans 에 - 추가하고
        num.pop(0)                  # num의 첫번째값을 지운다
    else:
        NO = True               # 그건 끝난거다.
        break
if NO:
    print('NO')
else:
    for i in ans:
        print(i)

