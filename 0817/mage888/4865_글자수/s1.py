import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    p = input()
    text = input()

    result = 0
    for i in p:
        cnt = 0
        for j in text:
            if i == j:
                cnt += 1

        if result < cnt:
            result = cnt

    print('#{} {}'.format(tc, result))