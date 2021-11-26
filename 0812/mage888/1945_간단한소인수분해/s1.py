import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())

    pn = []

    for i in range(2, 12):
        result = True
        for j in range(2, i):
            if i % j == 0:
                result = False
        if result:
            pn.append(i)

    pn_cnt = [0] * len(pn)

    for i in range(len(pn)):

        while True:

            if n % pn[i] == 0:
                n //= pn[i]
                pn_cnt[i] += 1
            else:
                break

    print('#{} {}'.format(tc, ' '.join(map(str, pn_cnt))))


