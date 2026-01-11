import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

def bfs(sr, sc):
    # 상어의 초기 상태
    cr, cc = sr, sc
    size = 2
    size_cnt = 0
    total_mx = 0 # mx를 누적할 전체 시간 변수

    while True:
        q = deque([(cr, cc, 0)])
        visited = [[False] * N for _ in range(N)]
        visited[cr][cc] = True
        
        candidates = [] # 먹을 수 있는 물고기 후보들
        min_dist = float('inf')

        while q:
            curr_r, curr_c, cnt = q.popleft()
            
            # 이미 찾은 최단 거리보다 멀어지면 탐색 중단
            if cnt >= min_dist:
                continue

            for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                nr, nc = curr_r + dr, curr_c + dc
                
                if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                    # 지나갈 수 있는 조건
                    if arr[nr][nc] <= size:
                        visited[nr][nc] = True
                        
                        # 먹을 수 있는 조건
                        if 0 < arr[nr][nc] < size:
                            candidates.append((cnt + 1, nr, nc))
                            min_dist = cnt + 1
                        else:
                            q.append((nr, nc, cnt + 1))
        
        # 더 이상 먹을 물고기가 없으면 종료
        if not candidates:
            break
            
        # 거리가 가장 가깝고, 위쪽, 왼쪽 순으로 정렬
        candidates.sort()
        dist, nr, nc = candidates[0]
        
        # 사냥 결과 반영
        total_mx += dist # 이번 사냥에 걸린 거리를 전체 시간에 누적
        size_cnt += 1
        if size_cnt == size:
            size += 1
            size_cnt = 0
        
        arr[nr][nc] = 0 # 물고기 먹음
        cr, cc = nr, nc # 상어 위치 갱신
        
        # 로그 출력 (필요 시 주석 해제)
        # print('(', nr, ',', nc, ') , mx =', total_mx, 'size:', size)

    return total_mx

# 상어 위치 찾기
answer = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            arr[i][j] = 0
            answer = bfs(i, j)

print(answer)