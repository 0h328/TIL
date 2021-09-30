import sys
sys.stdin = open('input.txt')

T = int(input())

for case in range(T):
    N = float(input())
    i = 1
    res = 0
    pos = []
    while N > 0:
        if 2 ** (-i) > N:
            i += 1
            continue

        N -= (2 ** (-i))
        pos.append(i)


    if len(pos) <= 12:
        final_pos = [0] * max(pos)
        for p in pos:
            final_pos[p - 1] = 1
        print('#{} {}'.format(case + 1, ''.join(map(str,final_pos))))
    else:
        print('#{} {}'.format(case + 1, 'overflow'))




