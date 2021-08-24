import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    num = list(input())
    stack = []
    result = []
    fin = []
    for i in range(N):
        if num[i] == '+' and stack:
            result.append(num[i])
        elif num[i] == '+':
            stack.append(num[i])
        else:
            result.append(num[i])
    while stack:
        result.append(stack.pop())

    for i in range(N):
        if result[i] == '+':
            fin.append(fin.pop() + fin.pop())
        else:
            fin.append(int(result[i]))
    while fin:
        print('#{} {}'.format(tc, fin.pop()))
