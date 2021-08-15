# 방법 1 - while

import sys
sys.stdin = open('input.txt')

def solve_while(target, pattern, N, M):

    i = 0
    j = 0
    while i < N and j < M:
        if target[i] != pattern[j]:
            i -= j
            j = -1
        i += 1
        j += 1
    if j == M:
        return i - M

target = input()
N = len(target)

pattern = input()
M = len(pattern)

ans = solve_while(target, pattern, N, M)
print('{}'.format(ans))		# 2
