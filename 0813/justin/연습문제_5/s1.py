def solve_while(target, pattern, N, M):
    # i -> 전체(target) 텍스트의 인덱스 - N
    # j -> 패턴(pattern) 텍스트의 인덱스 - M
    i = j = 0

    while j < M and i < N:           # i, j가 전체 & 패턴 길이보다 작을 때 문자를 하나씩 체크해보자
        if target[i] != pattern[j]:  # 만약 해당 인덱스의 문자끼리 서로 일치하지 않으면
            i = i - j                # 전체 인덱스는 경우 다시 0으로 (#3에서 한 칸 전진) -> 비교를 시작하는 위치로 돌려놓자
            j = -1                   # 패턴 인덱스의 경우 -1로 초기화 (밑에서 다시 0으로 만들어 주기 위함)

        # 일치하면 -> 둘 다 그냥 다음 문자 확인
        # 일치하지 않는다면
            # target 문자열은 처음에 확인했던 다음부터 다시 확인
            # pattern 인덱스는 다시 처음으로 돌아가서 확인
        i += 1 # target 문자에서 일치하지 않은 부분부터 다시 비교 시작
        j += 1 # 다시 target 인덱스(i)의 위치에서 pattern 인덱스의 시작(0)부터 비교하기 위함

    if j == M:         # 반복이 다 끝나고 패턴 인덱스와 패턴 문자의 길이가 같으면
        return i - M   # 전체 인덱스 - 패턴 길이 -> 찾고자 하는 첫 인덱스
    else:              # 길이가 다르면 매칭되지 않은 것
        return -1

def solve_for(target, pattern, N, M):
    for i in range(N-M+1):                # 전체 길이-찾아야 하는 길이+1
        cnt = 0
        for j in range(M):                # 찾을 텍스트의 길이(M)
            if target[i+j] != pattern[j]: # 전체(target) 텍스트와 패턴(pattern) 텍스트의 길이를 계속 확인하며 일치하지 않으면 다음 구간(i+1) 확인
                break
            else:                         # 일치하는 경우 -> count
                cnt += 1
        if cnt >= M:                      # 해당 구간(i)에서 반복이 마무리 되고 cnt가 찾아야 하는 문자(pattern)의 길이보다 크거나 같은 시점에
            return i                      # 그 인덱스 리턴 -> i인 이유는? pattern text와 일치하는 target text의 첫 번째 인덱스
    return -1                             # 못찾으면 -1

import sys
sys.stdin = open('input.txt')
target = input()      # 전체 텍스트
N = len(target)       # target의 길이

pattern = input()     # target 텍스트 내에서 찾아야 pattern 텍스트
M = len(pattern)      # pattern의 길이

# 방법 1 - while
# target과 일치하는 pattern 문자가 발견되는 첫 번째 index 반환
ans = solve_while(target, pattern, N, M)
print('{}'.format(ans))

# 방법 2 - for
# target과 일치하는 pattern 문자가 발견되는 첫 번째 index 반환
ans2 = solve_for(target, pattern, N, M)
print('{}'.format(ans2))

# 방법 3 - .find() 활용
# target과 일치하는 pattern 문자가 발견되는 첫 번째 index 반환
print(target.find(pattern))
