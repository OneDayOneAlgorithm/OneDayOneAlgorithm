import sys
input = sys.stdin.readline


def A():
    ans = sum(lst) / N
    return round(ans)


def B():
    return sorted_lst[N//2]


def C():                                # 최빈값 구하기
    visited = [0]*8001                  # 방문크기는 8001개 (-4000~4000)
    for i in lst:
        visited[i+4000] += 1            # 방문기록에 입력 배열+4000을 넣는다.
    max_v = max(visited)
    for i in range(8001):               # 방문기록을 싹 둘러봐서
        if visited[i] == max_v:             # 해당 인덱스를 방문했을 시
            c_lst.append(i-4000)        # 그방 인덱스를 리스트에 추가
    if len(c_lst) >= 2:
        return c_lst[1]
    else:
        return c_lst[0]


def D():
    if len(lst) >= 2:
        return (sorted_lst[-1] - sorted_lst[0])
    else:
        return 0


N = int(input())
lst = []
c_lst = []
for i in range(N):
    lst.append(int(input()))       # 입력 배열
sorted_lst = sorted(lst)            # 오름차 순으로 정렬
print(A())
print(B())
print(C())
print(D())
