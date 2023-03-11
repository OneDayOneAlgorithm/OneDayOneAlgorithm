def solve(n):
    if len(n) == len(A):    # 입력값의 자릿수가 A와 일치하고
        if int(n) < B and n[0] != '0':  # B보다 크고 맨 앞자리 수가 0이 아니면
            lst.append(int(n))  # 이를 리스트에 추가한다
            return
        else:
            return
    for i in range(len(A)):
        if used[i] == 0:
            used[i] = 1 # 사용한 숫자를 재사용하지 않기위해 구분한다.
            solve(n+A[i])   # 재귀를 돌린다.
            used[i] = 0

A,B = map(int,input().split())
A = str(A)
used = [0]*len(A)
lst = []
solve('')
if lst: 
    print(max(lst)) # 리스트의 숫자중 가장 큰 숫자를 출력한다.
else:   # 리스트가 비었을 경우에는 -1을 출력한다.
    print(-1)
