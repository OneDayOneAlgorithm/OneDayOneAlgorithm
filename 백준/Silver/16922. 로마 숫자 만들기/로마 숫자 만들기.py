def solve(n):
    global cnt, ans,sumv
    if cnt == N:               
        if sumv not in lst:     # 원소의 합이 중복되지 않도록 한다.
            lst.append(sumv)
            ans += 1
        return
    for i in range(n,4):       
        cnt += 1
        sumv += arr[i]
        solve(i)
        sumv -= arr[i]
        cnt -= 1
N = int(input())
cnt = 0
ans = 0
lst = []
sumv = 0
arr=[1,5,10,50]
solve(0)
print(ans)