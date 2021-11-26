import sys
sys.stdin = open('input.txt')


def perm(depth, acc_sum):   # 재귀 깊이 = 현재 인덱스, 누적합
    global ans

    if acc_sum >= ans:      # 이미 누적합이 ans 이상이면
        return              # 볼 필요 없음

    if depth == N:
        if ans > acc_sum:
            ans = acc_sum
        return

    for i in range(depth, N):   # 지금 인덱스부터 끝까지 순회
        case[i], case[depth] = case[depth], case[i]
        perm(depth+1, acc_sum + V[depth][case[depth]])  # 한번 더 깊어짐
        case[i], case[depth] = case[depth], case[i]


for tc in range(int(input())):
    N = int(input())
    V = [tuple(map(int, input().split())) for _ in range(N)]

    ans = 960217

    # ex> N=3일 때, [0,1,2], [0,2,1], ... , [2,1,0]을 만들고 싶음
    case = [n for n in range(N)]
    perm(0, 0)  # 재귀 깊이 = 지금 보고 있는 인덱스, 누적합

    print('#{0} {1}'.format(tc+1, ans))
    # break
