import math
import sys
from itertools import permutations
input = sys.stdin.readline
N = int(input())
numbers = list(input().split())
operator_list = list(map(int,input().split()))
operators = {0:'+',1:'-',2:'*',3:'/'}
operators_perm = []
for i in range(4):
    if operator_list[i] != 0:
        for _ in range(operator_list[i]):
            operators_perm.append(operators[i])
perm = set(permutations(operators_perm,len(numbers)-1))
max_v,min_v = -math.inf,math.inf
for i in perm:
    i = list(i)
    stack = []
    for j in range(len(numbers)):
        stack.append(numbers[j])
        if len(stack) == 3:
            calulation = int(eval(''.join(stack)))
            stack = [str(calulation)]
        if j == len(numbers)-1:
            break
        else:
            stack.append(i[j])
    ans = eval(''.join(stack))
    if ans > max_v:
        max_v = ans
    if ans < min_v:
        min_v = ans
print(max_v)
print(min_v)
