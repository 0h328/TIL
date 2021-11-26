def solve(target, pattern):
    typo = cnt = 0
    T = len(target)
    P = len(pattern)
    while typo < T:                         # 빠른 글자가 전체 글자수를 넘지 않을 때까지 반복
        if target[typo:typo+P] == pattern:  # target에서 pattern을 찾으면
            typo += P                       # typo를 P만큼 추가 (일치하는 문자 다음부터 확인하기 위함)
            cnt += 1                        # 타이핑 1회 cnt
        else:                               # 못찾으면
            typo += 1                       # 한칸 앞으로 가서 다음 문자 확인
            cnt += 1                        # 타이핑 1회 cnt
    return cnt

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    target, pattern = input().split()
    ans = solve(target, pattern)
    print('#{} {}'.format(tc, ans))