import sys
N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
# 위치 담을 리스트
pos = []
dr = [0,0,1,-1]
dc = [1,-1,0,0]
# 상대돌을 따먹기위한 좌표 & 이때 따먹는 상대 돌의 갯수를 저장할 리스트
group = []

# 상대를 따먹는 좌표와 그때 몇개를 따먹는지 구해서 이 두개의 값을 group 리스트에 넣는다.
def bfs(cr,cc):
    board[cr][cc] = -1
    cnt = 0
    q = [(cr,cc)]
    # 상대돌을 따먹기 위한 좌표의 집합
    needs = set()
    while q:
        cr,cc = q.pop(0)
        # 상대 돌을 하나 더 따먹는다.
        cnt += 1
        for dir in range(4):
            nr = cr + dr[dir]
            nc = cc + dc[dir]
            # 현재위치에서 상하좌우가 맵 밖을 벗어나지 않고 & 사용하지 않았고 & 빈 지역일 때
            if 0<=nr<N and 0<=nc<M and (nr,nc) not in needs and not board[nr][nc]:
                # 상대돌을 따먹기 위한 좌표에 해당좌표 추가.
                needs.add((nr,nc))
            # 현재위치에서 상하좌우가 맵 밖을 벗어나지 않고 & 사용하지 않았고 & 상대 돌일 때
            if 0<=nr<N and 0<=nc<M and (nr,nc) not in needs and board[nr][nc] == 2:
                # 그 지역을 2에서 -1로 바꾸고
                board[nr][nc] = -1
                # q에 추가
                q.append((nr,nc))
    # 상대돌을 두번안에 따먹을 수 있다면
    if len(needs) <= 2:
        # 상대돌을 따먹기위한 좌표 & 이때 따먹는 상대 돌의 갯수를 group이라는 리스트에 저장.
        group.append((needs,cnt))
ans = 0
cur_group = []

# 이제 상대를 따먹을 수 있는 모든 경우의 수의 좌표들에 돌을 둬보고 그중 가장 많이 따먹는 경우를 찾는다.
def combi(cnt,start,edges,count):
    global ans
    # 돌을 두개 넘게 놓으면 재귀 종료
    if len(edges) > 2:
        return
    # 상대돌을 가장 많이 따먹었을 때의 갯수를 ans에 넣는다.
    ans = max(ans,cnt)
    if count == len(group):
        return
    # (상대돌을 따먹기위한좌표,이때 따먹는 상대돌의 갯수) 형식. 이를 cur_group에 넣어준다.
    for i in range(start, len(group)):
        cur_group.append(group[i])
        # cur_group의 첫번째 원소인, 상대돌을 따먹기위한 좌표의 집합이 cur_set이다. 중복되지 않게 set 배열을 쓴다.
        cur_set = set(edges)
        for e in group[i][0]:
            cur_set.add(e)
        # 총 4개의 인자.
        # 1. 현재 따먹은 돌의 갯수.
        # 2. 순열(모든 경우의 수)를 만들기 위한 값.
        # 3. 따먹기 위한 좌표의 집합.
        # 4. 몇번째 그룹이냐. 그룹의 인덱스.
        combi(cnt+group[i][1], i+1, cur_set,count+1)
        cur_group.pop()

for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            bfs(i,j)

combi(0,0,set(),0)

print(ans)