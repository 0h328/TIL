def solve_while(target, pattern, N, M):
    idx = 0
    while idx < N-M+1:
        pattern_idx = 0
        while pattern_idx < M:
            if target[idx + pattern_idx] != pattern[pattern_idx]:
                break
            pattern_idx += 1
        else:
            return idx

        idx += 1

    return '일치하는게 없습니다.'

def solve_for(target, pattern, N, M):
    for i in range(N-M+1):
        for j in range(M):
            if target[i+j] != pattern[j]:
                break
        else:
            return i
    return '일치하는게 없습니다.'


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