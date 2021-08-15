# 방법 2 - for

import sys
sys.stdin = open('input.txt')

def solve_for(target, pattern, N, M):

    result = 0
    for i in range((N//2) + 1):
        if target[i:M+i] == pattern:
            result = target.index(pattern)

    return result

target = input()
N = len(target)

pattern = input()
M = len(pattern)

ans2 = solve_for(target, pattern, N, M)
print('{}'.format(ans2))    # 2