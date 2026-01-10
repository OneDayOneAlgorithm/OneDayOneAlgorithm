import sys
from collections import deque

def solve():
    A, B = map(int, sys.stdin.readline().split())
    q = deque([(A, 1)]) # (현재 숫자, 연산 횟수)
    visited = {A}

    while q:
        curr, dist = q.popleft()
        
        if curr == B:
            print(dist)
            return

        for next_val in (curr * 2, int(str(curr) + '1')):
            if next_val <= B and next_val not in visited:
                visited.add(next_val)
                q.append((next_val, dist + 1))
                
    print(-1)

solve()