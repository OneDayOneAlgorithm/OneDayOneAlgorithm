
N = input()
sum = ''
for i in N:
    if i.isupper():
        sum += i.lower()
    else:
        sum += i.upper()
print(sum)
