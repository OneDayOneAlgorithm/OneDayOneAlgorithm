def solution(s):
    answer = list(map(int,s.split()))
    mx = max(answer)
    mn = min(answer)
    answer = str(mn) + " " + str(mx)
    return answer