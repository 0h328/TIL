import sys

sys.stdin = open('input.txt')


# 순열 만들면서 계산
def gen_permutation(N, depth):
    global min_sum
    global temp_sum

    if temp_sum > min_sum:
        return

    if depth == N:
        if temp_sum < min_sum:
            min_sum = temp_sum
        return

    for i in range(N):
        if chosen[i]:
            continue
        chosen[i] = True
        temp_sum += nums[depth][i]
        gen_permutation(N, depth + 1)
        chosen[i] = False
        temp_sum -= nums[depth][i]


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    nums = [list(map(int, input().split())) for _ in range(N)]

    # 순열 리스트 생성
    chosen = [False] * N
    min_sum = 9 * N
    temp_sum = 0 # 변수 생성 순서 중요! NameError
    gen_permutation(N, 0)

    print('#{} {}'.format(t, min_sum))
