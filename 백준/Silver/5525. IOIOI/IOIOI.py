import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
s = input().rstrip()

ans, cor = 0,1
start = False
OI, OIb = ["O","I"], False
for i in range(m):
    if start == False and s[i] == "I":
        start = True
        OIb = False
        continue
    if start:
        if s[i] == OI[OIb]:
            if OIb == True:
                cor += 1
            OIb = not OIb
            continue
        else:
            if s[i] == "O":
                start = False
    ans += max(0,cor-n)
    OIb = False
    cor = 1
    
ans += max(0,cor-n)
print(ans)