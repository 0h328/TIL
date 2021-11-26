# slicing
# python은 slicing 할 때 범위 유의
def solve(pattern, target):
    M = len(target)
    N = len(pattern)
    cnt = 0
    for i in range(M-N+1):
        if pattern == target[i:i+N]: # 슬라이싱을 활용하여 같은지 여부를 확인
            cnt += 1                 # 카운트 업
    return cnt

import sys
sys.stdin = open('input.txt', encoding='UTF8')
for _ in range(1, 11):
    tc = input()
    pattern = input()
    target = input()
    ans = solve(pattern, target)
    print('#{} {}'.format(tc, ans))