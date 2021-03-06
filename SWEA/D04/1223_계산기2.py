def ip(x):
    if x == '*':
        return 2
    elif x == '+':
        return 1


def calc(operator, y, x):
    if operator == '+':
        return int(x) + int(y)
    elif operator == '*':
        return int(x)*int(y)


for tc in range(1, 11):
    input()
    stack = []
    result = ''
    for i in input():
        if i not in ['+', '*']:
            result += i
        else:
            while stack:
                if ip(i) > ip(stack[-1]):
                    stack.append(i)
                    break
                else:
                    result += stack.pop()
            else:
                stack.append(i)
    while stack:
        result += stack.pop()

    for i in result:
        if i not in ['+', '*']:
            stack.append(i)
        else:
            stack.append(calc(i, stack.pop(), stack.pop()))
    print(f'#{tc} {stack.pop()}')
