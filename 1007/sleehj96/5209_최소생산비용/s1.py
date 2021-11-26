# TimeError

import sys
sys.stdin = open('input.txt')


def perm(depth):
    global ans

    if depth == N:

        acc_sum = 0
        for idx in range(N):
            acc_sum += V[idx][case[idx]]

        if ans > acc_sum:
            ans = acc_sum
        return

    for i in range(depth, N):   # 지금 인덱스부터 끝까지 순회
        case[i], case[depth] = case[depth], case[i]
        perm(depth+1)           # 한번 더 깊어짐
        case[i], case[depth] = case[depth], case[i]


for tc in range(int(input())):
    N = int(input())
    V = [tuple(map(int, input().split())) for _ in range(N)]

    ans = 960217

    # ex> N=3일 때, [0,1,2], [0,2,1], ... , [2,1,0]을 만들고 싶음
    case = [n for n in range(N)]
    perm(0)  # 재귀 깊이 = 지금 보고 있는 인덱스

    print('#{0} {1}'.format(tc+1, ans))
    # break
