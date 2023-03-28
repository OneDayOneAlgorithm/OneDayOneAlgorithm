def solve(n,sum_v):
    global cnt
    if n == N:  # n은 0부터 시작이므로 최대 N-1 까지 유효하다.
        return
    if sum_v+arr[n] == S:   # 현재 값을 더했을 때 S가 되면
        cnt += 1            # 카운트
    solve(n+1,sum_v+arr[n])     # 처음엔 모든 원소를 포함하는 경우
    solve(n+1,sum_v)            # 두번째론 마지막 원소를 제외하는 경우
                                # 세번째는 끝에서 두번째 원소를 제외하고 마지막 원소를 포함하는 경우
                                # 등등..
N,S = map(int,input().split())
arr = list(map(int,input().split()))
cnt = 0
solve(0,0)
print(cnt)