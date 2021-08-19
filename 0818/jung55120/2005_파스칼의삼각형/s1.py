import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    stack = [[0]*n for _ in range(n)]
    for i in range(n): # i = 행번호
        stack[i][0] = 1
        for j in range(n): # j = 열번호
            if i > 0 and j > 0:
                stack[i][j] = stack[i-1][j-1] + stack[i-1][j]
    result = ''
    for k in range(n):
        for l in range(n):
            if stack[k][l] != 0:
                result += str(stack[k][l]) + ' '
        if k != n-1:
            result += '\n'

    print('#{0} \n{1}'.format(tc, result))
    #     result += ' '.join(map(str, stack[m])) + '\n'
    # print(result)

    #     stack[m] = str(int(''.join(stack[m])))
    # print(stack)
    # print(result)
