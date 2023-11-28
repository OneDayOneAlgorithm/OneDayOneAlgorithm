T = int(input())
lst = [0]*102
lst[1] = 1
lst[2] = 1
for i in range(3,102):
    lst[i] = lst[i-3]+lst[i-2]
for _ in range(T):
    N = int(input())
    print(lst[N])


    
