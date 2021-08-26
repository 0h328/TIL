def get_count_for_searching_page(total_page, search_page):
    l = 1
    r = total_page
    cnt = 0

    while True:
        c = int((l + r) / 2)
        if c < search_page:
            l = c
        elif c > search_page:
            r = c
        else:
            break
        cnt += 1
    return cnt

import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):

    P, Pa, Pb = map(int, input().split())
    a_ret = get_count_for_searching_page(P, Pa)
    b_ret = get_count_for_searching_page(P, Pb)

    if a_ret > b_ret:
        print('#{} {}'.format(tc, 'B'))
    elif a_ret < b_ret:
        print('#{} {}'.format(tc, 'A'))
    else:
        print('#{} {}'.format(tc, 0))

