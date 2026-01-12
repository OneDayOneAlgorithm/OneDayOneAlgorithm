import sys
from collections import deque

input = sys.stdin.readline
N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 첫번째노드
# 그 노드에서 갈수있는 모든 나라 체크
# 그 q 원소들을 리스트에 저장해서 평균값구하고 arr에서 값 변경
# 변경된 나라들은 방문체크되잇으니 다음날 될대까지 접근불가
# 하나라도 개통되는 나라가 있으면 이것을 계속 반복

def bfs(sr, sc):
    q = deque([(sr, sc)])
    lst = [(sr, sc)]
    pass_yn = False
    visited[sr][sc] = True
    while q:
        cr, cc = q.popleft()
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < N and 0 <= nc < N and (visited[nr][nc] == False) and (L <= abs(arr[nr][nc] - arr[cr][cc]) <= R):
                pass_yn = True
                lst.append((nr, nc))
                visited[nr][nc] = True
                q.append((nr, nc))
    sm = 0
    for r, c in lst:
        sm += arr[r][c]
    
    avg = sm // len(lst)
    for r, c in lst:
        arr[r][c] = avg
    if pass_yn == False:
        return -1
    else:
        return 0

result = 0
answer = 0
while True:
    visited = [[False] * N for _ in range(N)]
    next_day = False
    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                result = bfs(i, j)
                if result == 0:
                    next_day = True
    if next_day == True:
        answer += 1
    else:
        break

print(answer)