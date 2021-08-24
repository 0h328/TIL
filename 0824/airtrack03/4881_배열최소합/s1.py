import sys
from itertools import permutations
sys.stdin = open('input.txt')

T = int(input())

def permutation(idx, total):
    global ans      # idx == N 되어 해당 순열의 합 계산할 때, ans보다 작으면 갱신해줘야 하므로 global 활용

    if idx == N:    # 순열 완성
        if total < ans:
            ans = total
        return

    if total >= ans:
        return

    for i in range(N):
        if check[i] == 0:
            check[i] = 1
            total += data[idx][i]
            permutation(idx+1, total)
            total -= data[idx][i]
            check[i] = 0

for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    ans = 10 * N        # 각 숫자가 10 미만 자연수이므로 무조건 10*N보다 작음

    sel = [0] * N       # 순열을 만들기 위한 리스트
    check = [0] * N     # 현재 순열에 들어가있는 숫자 체크 위한 리스트

    permutation(0, 0)

    # for permutation in permutations(for_permutation, N):
    #     temp = 0
    #     for i in range(N):
    #         temp += data[i][permutation[i]]
    #         if temp >= ans:
    #             break
    #     if temp < ans:
    #         ans = temp

    print('#{} {}'.format(tc, ans))