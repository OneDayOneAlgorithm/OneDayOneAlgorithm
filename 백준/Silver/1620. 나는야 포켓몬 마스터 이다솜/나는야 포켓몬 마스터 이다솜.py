# https://www.acmicpc.net/problem/1620
N,M = map(int,input().split())
lst = dict()
for i in range(1,N+1):
    lst[i] = input()
reverse_lst = dict(map(reversed,lst.items()))
for i in range(M):
    quiz = input()
    # 알파벳이면
    if quiz.isalpha():
        print(reverse_lst[quiz])
    # 숫자면
    else:
        print(lst[int(quiz)])

