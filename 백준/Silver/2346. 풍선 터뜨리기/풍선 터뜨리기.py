N = int(input())
arr = list(map(int,input().split()))
q = []
for i in range(N):
    q.append((i+1,arr[i]))
ans = []
idx = 0
while len(q) > 1:
    ans.append(q[idx][0])
    c = q[idx][1]
    q.pop(idx)
    if c >= 0:
        idx = (idx+c-1) % len(q)
    else:
        idx = (idx+c) % len(q)
ans.append(q[0][0])
print(*ans)
