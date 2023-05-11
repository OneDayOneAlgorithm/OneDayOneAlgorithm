from sys import stdin
import itertools 

input = stdin.readline

N = int(input())
mp,mf,ms,mv = map(int,input().split())
lst = [[]]
for _ in range(N):
    p,f,s,v,c = map(int,input().split())
    lst.append((p,f,s,v,c))

ans = 9875643210
ans_lst = []
for cnt in range(1,N+1):
    for i in itertools.combinations(range(1,N+1),cnt):
        p = 0
        f = 0
        s = 0
        v = 0
        price = 0
        for j in i:
            p += lst[j][0]
            f += lst[j][1]
            s += lst[j][2]
            v += lst[j][3]
            price += lst[j][4]
        if p>=mp and f>=mf and s >=ms and v>=mv:
            if ans > price:
                ans = price
                ans_lst = i
            elif ans == price:
                ans_lst = sorted((ans_lst,i))[0]
if ans == 9875643210:
    print(-1)
else:
    print(ans)
    print(*ans_lst)


    
