def div(num): # 복도로 변환
    return (int(num)+1) // 2

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    students = [list(map(div, input().split())) for _ in range(N)]

    corridor = [0] * 201

    for i in range(N):
        if students[i][0] > students[i][1]:
            students[i][0], students[i][1] = students[i][1], students[i][0]

        for j in range(students[i][0], students[i][1]+1):
            corridor[j] += 1

    print('#{} {}'.format(tc, max(corridor)))