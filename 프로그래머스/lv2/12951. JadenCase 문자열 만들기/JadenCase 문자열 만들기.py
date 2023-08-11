def solution(a):
    s = list(str(a).lower())
    s[0]=s[0].upper()
    for i in range(len(s)-1):
        if s[i] == ' ':
            if s[i+1] == ' ':
                continue
            s[i+1] = s[i+1].upper()
    return ''.join(s)