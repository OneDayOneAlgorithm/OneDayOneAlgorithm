lst = [0]*41
lst[0] = (1,0)
lst[1] = (0,1)
for i in range(2,41):
    lst[i]=(lst[i-1][0]+lst[i-2][0],lst[i-1][1]+lst[i-2][1])
T = int(input())
for _ in range(T):
    N = int(input())
    print(*lst[N])