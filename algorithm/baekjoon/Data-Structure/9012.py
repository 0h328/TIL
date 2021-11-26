import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    brackets = list(input())

    cnt = 0
    for bracket in brackets:
        if bracket == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            break

    if cnt == 0:
        print('YES')
    else:
        print('NO')
