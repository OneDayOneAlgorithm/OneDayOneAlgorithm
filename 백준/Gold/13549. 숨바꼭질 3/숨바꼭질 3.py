import sys
from collections import deque

input = sys.stdin.readline
N, K = map(int, input().split())

def bfs(N, K):
    # 0부터 100,000까지 방문 체크 및 시간 저장
    visited = [-1] * 100001
    q = deque([N])
    visited[N] = 0

    while q:
        ci = q.popleft()

        if ci == K:
            return visited[ci]

        # 1. 순간이동 (0초 소요) - 가장 높은 우선순위
        ni_teleport = ci * 2
        if ni_teleport <= 100000 and visited[ni_teleport] == -1:
            visited[ni_teleport] = visited[ci]
            # 0초 걸리는 곳은 큐의 '앞'에 넣어서 먼저 처리되게 함!
            q.appendleft(ni_teleport)

        # 2. 걷기 (1초 소요)
        for ni in [ci - 1, ci + 1]:
            if 0 <= ni <= 100000 and visited[ni] == -1:
                visited[ni] = visited[ci] + 1
                # 1초 걸리는 곳은 큐의 '뒤'에 넣음
                q.append(ni)
    return 0

print(bfs(N, K))