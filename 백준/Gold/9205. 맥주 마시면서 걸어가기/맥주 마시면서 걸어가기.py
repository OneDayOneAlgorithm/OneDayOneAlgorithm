import sys, copy
from collections import deque

def bfs(sr, sc, er, ec, convenienceStores):
    q = deque([(sr, sc)])
    visited = [False] * len(convenienceStores)
    while q:
        cr, cc = q.popleft()
        if abs(cr - er) + abs(cc - ec) <= 1000:
            return 'happy'
        for i in range(len(convenienceStores)):
            if not visited[i]:
                nr, nc = convenienceStores[i]
                if abs(cr - nr) + abs(cc - nc) <= 1000:
                    visited[i] = True
                    q.append((nr, nc))
    return 'sad'

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    convenienceStores = []
    sr, sc = map(int,input().split())
    for _ in range(n):
        a, b = map(int,input().split())
        convenienceStores.append((a, b))
    er, ec = map(int,input().split())
    answer = bfs(sr, sc, er, ec, convenienceStores)
    print(answer)