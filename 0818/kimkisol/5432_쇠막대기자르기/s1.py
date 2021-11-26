import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    case = input()
    sticks = 0
    idx = 0
    result = 0
    while idx < len(case):
        if case[idx:idx + 2] == '()':
            result += sticks #잘랐을때 막대기 개수 추가되는 것
            idx += 2
        elif case[idx] == '(':
            sticks += 1
            idx += 1
        elif case[idx] == ')':
            sticks -= 1
            result += 1 #원래 막대기 개수 세기
            idx += 1

    print('#{} {}'.format(t, result))
