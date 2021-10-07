import sys
sys.stdin = open('input.txt')


def perm(depth, acc_mul):   # 깊이, 누적곱
    global ans

    if acc_mul <= ans:
        return

    if depth == N:
        if ans < acc_mul:
            ans = acc_mul
        return

    for i in range(depth, N):
        case[depth], case[i] = case[i], case[depth]
        perm(depth+1, acc_mul * (percentages[depth][case[depth]]))
        case[depth], case[i] = case[i], case[depth]


for tc in range(int(input())):
    N = int(input())
    percentages = [tuple(map(lambda x: int(x)/100, input().split())) for _ in range(N)]

    ans = 0
    case = [n for n in range(N)]
    perm(0, 100)    # 재귀 깊이, 누적곱

    print('#{0} {1:.6f}'.format(tc+1, ans))
    break
