# https://www.acmicpc.net/problem/11723
import sys

input = sys.stdin.readline

M = int(input())
S = []
for _ in range(M):
    put = input().strip()
    if put == "all":
        S = []
        for i in range(1,21):
            S.append(i)
    elif put == "empty":
        S = []
    else:
        cal, x = put.split()
        x = int(x)
        if cal == "add":
            if x not in S:
                S.append(x)
        if cal == "remove":
            while x in S:
                S.remove(x)
        if cal == "check":
            if x in S:
                print(1)
            else:
                print(0)
        if cal == "toggle":
            if x in S:
                while x in S:
                    S.remove(x)
            else:
                S.append(x)

