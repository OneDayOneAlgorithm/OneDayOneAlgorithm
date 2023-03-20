N,K = map(int,input().split())
q = list(i for i in range(1,N+1))
ans = []
idx = K-1
while len(q)>1:
    ans.append(q.pop(idx))
    idx = (idx+K-1)%len(q)
ans.append((q[0]))
print('<',end='')
for i in range(N-1):
    print(ans[i],end=', ')
print(f'{ans[N-1]}>')