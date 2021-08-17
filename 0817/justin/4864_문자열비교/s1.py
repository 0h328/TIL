def solve(pattern, target):
    j = 0            # pattern idx
    i = 0            # target idx
    P = len(pattern)
    T = len(target)

    while j < P and i < T:          # 종료 조건
        if pattern[j] != target[i]: # 다른 경우
            i = i - j               # target의 다음 인덱스
            j = -1                  # pattern의 처음으로 이동
        i += 1
        j += 1

    if j == len(pattern):   # pattern의 길이와 pattern을 체크하는 인덱스(j)가 같아지면 회문
        return 1
    else:
        return 0

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    pattern = input()
    target = input()
    ans = solve(pattern, target)
    print('#{} {}'.format(tc, ans))