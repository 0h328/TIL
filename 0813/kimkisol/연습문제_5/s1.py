import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def solve_while(target, pattern, N, M):
    target_idx = 0
    pattern_idx = 0
    cnt = 0
    while target_idx < N:
        if cnt == M:
            return target_idx
        if target[target_idx + pattern_idx] != pattern[pattern_idx]:
            target_idx += 1
            pattern_idx = 0
            cnt = 0
            continue
        pattern_idx += 1
        cnt += 1
    return False


def solve_for(target, pattern, N, M):
    cnt = 0
    for target_idx in range(N - M):
        for pattern_idx in range(M):
            if target[target_idx + pattern_idx] != pattern[pattern_idx]:
                cnt = 0
                break
            cnt += 1
            if cnt == M:
                return target_idx
    return False


import sys
sys.stdin = open('input.txt')
target = input()
N = len(target)

pattern = input()
M = len(pattern)


# 방법 1 - while
# target과 일치하는 pattern 문자가 발견되는 첫 번째 index 반환
ans = solve_while(target, pattern, N, M)
print('{}'.format(ans))		# 2

# 방법 2 - for
# target과 일치하는 pattern 문자가 발견되는 첫 번째 index 반환
ans2 = solve_for(target, pattern, N, M)
print('{}'.format(ans2))	# 2

# 방법 3 - .find() 활용
# target과 일치하는 pattern 문자가 발견되는 첫 번째 index 반환
print(target.find(pattern)) # 2