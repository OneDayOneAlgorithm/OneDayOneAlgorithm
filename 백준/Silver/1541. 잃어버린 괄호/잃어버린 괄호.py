operation_list = ['+', '-']
operations = []
numbers = []
number = ''
form = list(input())
for i in form:
    if i in operation_list:
        numbers.append(int(number))
        number = ''
        operations.append(i)
        continue
    number += i
numbers.append(int(number))
numbers_sum = numbers[0]
for i in range(len(operations)):
    if operations[i] == '+':
        numbers_sum += numbers[i+1]
    else:
        operations = ['-'] * len(operations)
        numbers_sum -= numbers[i + 1]
print(numbers_sum)
