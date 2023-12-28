import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    MBTI = list(input().split())
    min_cnt = 9999
    if N > 32:
        print(0)
    else:
        for i in range(N):
            for j in range(i+1,N):
                for k in range(j+1,N):
                    cnt = 0
                    if i == j or j == k or i == k:
                        continue
                    for dir in range(4):
                        if MBTI[i][dir] != MBTI[k][dir]:
                            cnt += 1
                        if MBTI[j][dir] != MBTI[k][dir]:
                            cnt += 1
                        if MBTI[i][dir] != MBTI[j][dir]:
                            cnt += 1
                    if min_cnt > cnt:
                        min_cnt = cnt
        print(min_cnt)