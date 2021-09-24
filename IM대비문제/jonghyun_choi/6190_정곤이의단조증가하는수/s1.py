import sys
sys.stdin = open('input.txt')

T = int(input())

for case in range(T):
    N = int(input())
    data = list(map(str, input().split()))
    res = []
    for i in data:
        pos = ''
        for j in i:
            if not pos:
                pos += j
            elif pos[-1] <= j:
                pos += j
            else:
                break
        else:
            res.append(int(j))
    sorted_res = sorted(res)
    if len(res) < 2:
        print('#{} {}'.format(case + 1, -1))
    else:
        print('#{} {}'.format(case + 1, sorted_res[-1] * sorted_res[-2]))


