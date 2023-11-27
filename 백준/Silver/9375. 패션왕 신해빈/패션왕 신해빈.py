T = int(input())
for _ in range(T):
    n = int(input())
    dic = dict()
    sm = 1
    for _ in range(n):
        name, word = input().split()
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1
    for i in dic.values():
        sm *= i + 1
    print(sm - 1)