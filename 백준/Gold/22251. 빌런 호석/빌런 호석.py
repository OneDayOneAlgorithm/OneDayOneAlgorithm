# N : 최대 몇층인가
# K : 몇자리 수인가
# P : 최대 몇개를 반전시킬 것이냐
# X : 현재 숫자는 뭐냐
N,K,P,X = map(int,input().split())
dic = {'0':'1111110', '1':'0000110', '2':'1011011', '3':'1001111', '4':'0100111', '5':'1101101', '6':'1111101', '7':'1000110', '8':'1111111', '9':'1101111'}
# K자리 숫자형태로 만든다. (문자형)
X = str(X).zfill(K)
# 현재 무슨 숫자들로 이루어져 있는가
x_transform = [dic[i] for i in X]
# 만들수 있는 숫자의 갯수
possible_num = 0
# 1층부터 N층까지
for n in range(1,N+1):
    # 각 층에 대하여 그 층을 k 자리 숫자형태로 만든다.
    elevator = str(n).zfill(K)
    # 그것들은 무슨 숫자들로 이루어져 있는가
    ele_transform = [dic[e] for e in elevator]
    diff_cnt = 0
    # 현재 층과 각 층을 튜플로 묶어 현재층을 그 층으로 만들기 위해 몇개의 수를 변경해야하는지 찾는다.
    for x,e in zip(x_transform, ele_transform):
        # 숫자 하나하나를 비교하여 몇개의 숫자가 다른지 센다.
        for i,j in zip(x,e):
            if i != j:
                # 서로 다르다면 카운트한다.
                diff_cnt += 1
        # 너무 많이 달라서 제한 갯수인 P보다 커지면 그만세고 다음층으로 간다.
        if diff_cnt > P:
            break
    # 해당 층으로 만들기 위해 바꿔야할 신호의 갯수가 P개 이하라면 (0개면 같은 수이니 0도 제외한다.)
    if 0 < diff_cnt <= P:
        # 전체 카운트 1 을 해준다.
        possible_num += 1
print(possible_num)