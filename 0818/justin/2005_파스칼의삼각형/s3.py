def solve(line):
    result = [[] for _ in range(line)]
    for i in range(line):
        cnt = i + 1
        for j in range(cnt):
            if j == 0 or j == i:        # 처음 or 끝이면
                result[i].append(1)     # 1 추가
            else:                       # 중간이면
                val = result[i-1][j-1] + result[i-1][j] # 더하고 & 추가
                result[i].append(val)

    return [map(str, row) for row in result]

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print('#{}'.format(tc))
    ans = solve(N)
    for s in ans:
        print('{}'.format(' '.join(s)))