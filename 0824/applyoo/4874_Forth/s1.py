import sys
sys.stdin = open('input.txt')

T = int(input())
for test in range(T):
    data = list(map(str, input().split()))
    result = []

    for char in data:
        if char in ('+', '-', '*', '/'):
            try:
                num1 = result.pop()
                num2 = result.pop()
                if char == '+': result.append(num1+num2)
                elif char == '-': result.append(num2-num1)
                elif char == '*': result.append(num1*num2)
                else: result.append(num2//num1)
            except IndexError:
                print('#{} error'.format(test+1))
                break
        elif char == '.':
            if len(result) == 1:
                print('#{} {}'.format(test+1, result[0]))
            else:
                print('#{} error'.format(test + 1))
        else:
            result.append(int(char))
