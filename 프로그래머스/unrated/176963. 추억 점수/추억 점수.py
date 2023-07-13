def solution(name, yearning, photo):
    answer = []
    search = {}
    for i in range(len(name)):
        search[name[i]] = yearning[i] 
    for i in photo:
        result = 0
        for j in i:
            if j in name:
                result += search[j]
        answer.append(result)
    return answer