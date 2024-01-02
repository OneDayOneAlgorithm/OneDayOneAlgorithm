N, M = map(int, input().split())
lst_input = list(map(int,input().split()))
someone_who_knows = []
party = []
graph = [[] for _ in range(N+1)]
# 거짓말을 아는 사람 리스트
for i in range(1,lst_input[0]+1):
    someone_who_knows.append(lst_input[i])
# 그래프 만들기
for _ in range(M):
    lst_input = list(map(int,input().split()))
    party.append(lst_input[1:])
    for i in range(1,lst_input[0]+1):
        for j in range(1,lst_input[0]+1):
            if lst_input[i] != lst_input[j] and lst_input[j] not in graph[lst_input[i]]:
                graph[lst_input[i]].append(lst_input[j])

for i in range(1,N+1):
    q = [i]
    visited = [0] * (N + 1)
    while q:
        c = q.pop(0)
        for j in graph[c]:
            if not visited[j]:
                visited[j] = 1
                q.append(j)
                if c in someone_who_knows and j not in someone_who_knows:
                    someone_who_knows.append(j)
cnt = 0
for i in party:
    for j in i:
        if j in someone_who_knows:
            break
    else:
        cnt += 1

print(cnt)



# [0]*(N+1) 이후 비밀을 아는 사람은 1로 표현
# []*(N+1) 이후 비밀을 아는사람 기준으로 그래프를 돌려서 한번이라도 같은 파티에 있었던 사람(연관된 사람)은 비밀을 아는 사람으로 간주(someone_who_knows에 추가)
# someone_who_knows이 없는 파티 카운트
# 에러 : 예제 4번에서 에러남


