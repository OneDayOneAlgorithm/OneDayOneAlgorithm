T = int(input())
for _ in range(T):
    N,ans = map(int,input().split())
    arr = list(map(int,input().split()))
    q = []
    cnt = 1
    for i in range(N):
        q.append((arr[i],i))
    arr.sort(reverse=True)

    while q:
        if q[0][0] == arr[0]:
            if q[0][1] == ans:
                print(cnt)
                break
            q.pop(0),arr.pop(0)
            cnt += 1
        else:
            q.append(q.pop(0))


