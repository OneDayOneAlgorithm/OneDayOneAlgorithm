N,K = map(int,input().split())
lst = []
for _ in range(N):
    lst.append(int(input()))
lst.sort(reverse=True)
result = 0
i = 0
cnt = 0
while i<N:
    result += lst[i]
    if result > K:
        result -= lst[i]
        i += 1
    else:
        cnt += 1
print(cnt)