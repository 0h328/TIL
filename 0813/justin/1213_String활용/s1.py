# index
def solve(pattern, target):
    cnt = 0
    M = len(target)
    N = len(pattern)
    for i in range(M-N+1):                # 일반항
        for j in range(N):                # pattern 텍스트만큼 반복
            if pattern[j] != target[i+j]: # 다른 경우
                break                     # 종료
        else:                             # 매칭되었다면 (for-else)
            cnt += 1                      # 하나 카운트
    return cnt

import sys
sys.stdin = open('input.txt', encoding='UTF8')
for _ in range(1, 11):
    tc = input()
    pattern = input()
    target = input()
    ans = solve(pattern, target)
    print('#{} {}'.format(tc, ans))