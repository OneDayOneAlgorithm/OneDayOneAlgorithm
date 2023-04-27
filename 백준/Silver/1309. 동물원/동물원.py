N = int(input())
ans = [0]*(N+1)
for i in range(N+1):
    ans[i] = [0,0,0]
ans[1][0]=1
ans[1][1]=1
ans[1][2]=1

for i in range(2,N+1):
    ans[i][0] = (ans[i-1][0]+ans[i-1][1]+ans[i-1][2]) %9901
    ans[i][1] = (ans[i-1][0]+ans[i-1][2]) %9901
    ans[i][2] = (ans[i-1][0]+ans[i-1][1]) %9901
print(sum(ans[N]) % 9901)

