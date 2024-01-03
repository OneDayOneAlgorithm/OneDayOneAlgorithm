import sys
input = sys.stdin.readline

def func(v,distance):
    global instance_distance, c
    if distance > instance_distance:
        instance_distance = distance
        c = v
    for i in graph[v]:
        if not visited[i[0]]:
            visited[i[0]] = 1
            func(i[0],distance+i[1])

V = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(V):
    lst_input = list(map(int,input().split()))
    i = 1
    while lst_input[i] != -1:
        graph[lst_input[0]].append((lst_input[i],lst_input[i+1]))
        i += 2
max_distance = 0
q = [1]
lst = [1]
while q:
    i = q.pop(0)
    instance_distance = 0
    visited = [0] * (V + 1)
    visited[i] = 1
    func(i,0)
    if max_distance < instance_distance:
        max_distance = instance_distance
    lst.append(c)
    if len(lst)>=3 and lst[-1] == lst[-3]:
        break
    q.append(c)

print(max_distance)
