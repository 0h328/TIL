import sys

sys.stdin = open('input.txt')


def gen_permutation(n, depth, P):
    result = []
    if depth == n:
        return [P]
    else:
        for i in range(N):
            if chosen[i]:
                continue
            chosen[i] = True
            result += gen_permutation(n, depth + 1, P + [i])
            chosen[i] = False
    return result


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    nums = [list(map(int, input().split())) for _ in range(N)]

    # 순열 리스트 생성
    chosen = [False] * N
    perms = gen_permutation(N, 0, [])

    min_sum = 99999
    for i in range(len(perms)):
        result = 0
        for j in range(N):
            result += nums[perms[i][j]][j]
            if result > min_sum:
                break
        else:
            if result < min_sum:
                min_sum = result

    print('#{} {}'.format(t, min_sum))
