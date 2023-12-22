N, M = map(int,input().split())
radder = {}
snake = {}
for _ in range(N):
    x, y = map(int,input().split())
    radder[x]=y
for _ in range(M):
    x, y = map(int,input().split())
    snake[x]=y
cnt = [0]*101
visit = [0]*101
q = [1]
while q:
    cp = q.pop(0)
    if cp == 100:
        print(cnt[cp])
        break
    for i in range(1,7):
        np = cp + i
        if np <= 100 and not visit[np]:
            if np in radder.keys():
                np = radder[np]
            if np in snake.keys():
                np = snake[np]
            if not visit[np]:
                q.append(np)
                visit[np] = 1
                cnt[np] = cnt[cp] + 1

# 뱀은 무조건 피한다.
# 사다리를 내림차순으로 정리해 긴 사다리를 우선적으로 밟도록 한다.