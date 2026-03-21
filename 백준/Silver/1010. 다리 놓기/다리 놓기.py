import sys, math
from collections import deque
from itertools import permutations, combinations

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    # permutations(배열, 몇개씩 묶을건지) 를 사용하면 set형태로 나온다.
    print(math.comb(M, N))