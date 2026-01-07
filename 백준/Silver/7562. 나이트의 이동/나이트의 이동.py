import sys
from collections import deque

input = sys.stdin.readline

test_case = int(input())

def bfs(start_r, start_c, start_cnt):
    visited = [[False] * n for _ in range(n)]
    visited[start_r][start_c] = True
    q = deque([(start_r, start_c, start_cnt)])
    while q:
        current_r, current_c, current_cnt = q.popleft()
        if (current_r, current_c) == (end_r,end_c):
            return current_cnt
        for dr, dc in [(1,2),(1,-2),(2,1),(2,-1),(-1,2),(-1,-2),(-2,1),(-2,-1)]:
            next_r, next_c = current_r + dr, current_c + dc
            if 0 <= next_r < n and 0 <= next_c < n and visited[next_r][next_c] == False:
                visited[next_r][next_c] = True
                q.append((next_r, next_c, current_cnt + 1))
    return current_cnt

for _ in range(test_case):
    n = int(input())
    start_r, start_c = map(int,input().split())
    end_r, end_c = map(int,input().split())

    answer = bfs(start_r, start_c, 0)
    print(answer)