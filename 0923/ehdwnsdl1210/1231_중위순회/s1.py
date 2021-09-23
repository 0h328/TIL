def in_order(n):                    # 상좌우 / 좌상우 / 좌우상
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
    word = [0] * (N+1)              # 좌우뿐만 아니라 글자도 인덱스로 지정
    res = ''                        # 출력을 위해

    for _ in range(N):
        I = list(input().split())   # 그대로 하면 숫자도 글자로 받음
        # print(I)
        if len(I) > 3:                      # 자식 좌우 모두 존재
            left[int(I[0])] = int(I[2])
            right[int(I[0])] = int(I[3])
            word[int(I[0])] = I[1]

        elif len(I) > 2:                    # 자식 좌만 존재
            left[int(I[0])] = int(I[2])
            word[int(I[0])] = I[1]

        else:                               # 무자식
            word[int(I[0])] = I[1]

    print('#{} {}'.format(tc, in_order(1)))

