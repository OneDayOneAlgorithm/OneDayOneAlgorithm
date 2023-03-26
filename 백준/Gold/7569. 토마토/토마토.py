from collections import deque
import sys
input = sys.stdin.readline
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
def bfs():  # bfs 함수 시작
    while q:    # q 가 빌 때까지 실행
        cx, cy, cz = q.popleft()        # 현재 cx, cy, cz 에 값을 할당 (c는 current)
        visit[cz][cx][cy] = 1          # 현재 cx, cy, cz 방문 표시
        for dir in range(6):          # 모든 방향으로 이동
            nx = cx + dx[dir]
            ny = cy + dy[dir]
            nz = cz + dz[dir]
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and s[nz][nx][ny] == 0 and visit[nz][nx][ny] == 0:   # 범위 안 이거나 안썩은 토마토이거나 방문을 안한 곳일 시
                q.append([nx, ny, nz])     # q에 추가하고
                s[nz][nx][ny] = s[cz][cx][cy] + 1  # 그 전파된 값에 전의 값보다 1을 증가시킨 값을 넣는다.
                visit[nz][nx][ny] = 1   # 그리고 방문표시를 한다.
m, n, h = map(int, input().split())     # 가로, 세로, 높이를 입력을 받는다.
s = [[] for i in range(h)]  # h층으로 이루어진 빈 리스트를 만든다.
visit = [[[0 for i in range(m)] for i in range(n)] for i in range(h)]   # x,y,z 3중 배열인 방문기록을 만든다.
q = deque()  # q를 사용할 것이므로 빈 리스트를 만든다.
isTrue = False  # 나중에 이것이 True로 바뀌면 벽으로 갇혀서 썩지 않은 토마토가 생긴다는 의미다. 그때는 결과값으로 -1을 츨력한다.

for i in range(h):  # 매 높이마다
    for j in range(n):  # 매 행마다
        s[i].append(list(map(int, input().split())))    # 입력을 해준다.
for z in range(h):
    for x in range(n):
        for y in range(m):
            if s[z][x][y] == 1:
                q.append([x, y, z])
bfs()
max_num = 0
for z in range(h):
    for x in range(n):
        for y in range(m):
            if s[z][x][y] == 0:
                isTrue = True
            max_num = max(max_num, s[z][x][y])
if isTrue == True:
    print(-1)
else:
    print(max_num - 1)