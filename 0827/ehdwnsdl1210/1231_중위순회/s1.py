def in_order(n):
    global res
    if n:
        in_order(left[n])
        res += word[n]
        in_order(right[n])
    return res

import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    left = [0] * (N+1)
    right = [0] * (N+1)
    word = [0] * (N+1)
    res = ''

    for _ in range(N):
        I = list(input().split())   # 그대로 하면 숫자도 글자로 받음
        # print(I)
        if len(I) > 3:
            left[int(I[0])] = int(I[2])
            right[int(I[0])] = int(I[3])
            word[int(I[0])] = I[1]

        elif len(I) > 2:
            left[int(I[0])] = int(I[2])
            word[int(I[0])] = I[1]

        else:
            word[int(I[0])] = I[1]

    print('#{} {}'.format(tc, in_order(1)))

