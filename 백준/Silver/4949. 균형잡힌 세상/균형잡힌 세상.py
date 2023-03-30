arr = []
while True:
    n = input()
    if n == '.':
        break
    arr.append(n)
for s in arr:
    if s == '.':
        break
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        if i == '[':
            stack.append(i)
        if i == ')':
            if not stack or stack[-1] != '(':
                print('no')
                break
            else:
                stack.pop(-1)
        if i == ']':
            if not stack or stack[-1] != '[':
                print('no')
                break
            else:
                stack.pop(-1)
    else:
        if stack:
            print('no')
        else:
            print('yes')
