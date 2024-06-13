N = int(input())
people = list(map(int,input().split()))
T, P = map(int,input().split())
T_set = 0
for i in people:
    if not i:
        continue
    T_set += 1
    if i > T:
        T_set += i // T
        if not i % T:
            T_set -= 1
P_set = N // P
P_one = N % P
print(T_set)
print(P_set, P_one)