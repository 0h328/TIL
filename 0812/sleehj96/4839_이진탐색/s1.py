import sys

sys.stdin = open('input.txt')

T = int(input())
idx = 1

while idx <= T:
    P, Pa, Pb = map(int, input().split())
    cnt_a = cnt_b = 1

    l = 1
    r = P
    while l <= r:
        c = int((l + r) / 2)
        if Pa == c:
            break
        elif Pa < c:
            r = c
        else:
            l = c
        cnt_a += 1

    l = 1
    r = P
    while l <= r:
        c = int((l + r) / 2)
        if Pb == c:
            break
        elif Pb < c:
            r = c
        else:
            l = c
        cnt_b += 1

    # print(cnt_a, cnt_b)
    if cnt_a < cnt_b:
        ans = 'A'
    elif cnt_a > cnt_b:
        ans = 'B'
    else:
        ans = 0

    print('#{0} {1}'.format(idx, ans))

    idx += 1
