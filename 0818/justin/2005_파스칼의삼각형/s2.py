def solve(li1, li2):
    result = []
    for l1, l2 in zip(li1, li2):
        result.append(l1 + l2)
    return result

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    pascal = [1]
    print('#{}'.format(tc))
    for _ in range(N):          # N의 개수(row의 개수)만큼 반복
        print(*pascal)          # start 갱신
        """
        1. 아래와 같은 조합
        *start, 0
        0, *start

        2. 이 조합의 합이 result에 할당
        result = [1, 1]
        """
        pascal = solve([*pascal, 0], [0, *pascal])