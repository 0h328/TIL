#2. DP (with memoization) 활용
"""
피보나치 수열을 구할 때 N-2번째와 N-1번째 값을 알고 있으면 N번째 피보나치 값을 구할 수 있다. 
이를 응용하여 문제를 풀어보자

- 가지치기를 활용해서 시간을 줄이는 것이 아니라 memoization을 활용하여 시간을 줄여보자
- return value를 통해 값을 구하기 때문에 dist 변수를 따로 둘 필요가 없다.
"""

def solve(r, c):                          
    """
    매개변수 -> 문제를 식별하는 값
    반환값 -> 문제의 해(최솟값)
    """
    if r == 0 and c == 0:                   # 시작 위치 arr[0][0]에 돌아왔다면
        return arr[0][0]                    # 그 값을 반환

    # 1. -1이 아니라는 것은 이미 계산이 되었다는 의미 -> 계산된 값을 반환
    if memo[r][c] != -1:
        return memo[r][c]

    # 2. 아직 문제 해결이 안된 경우라면
    up = left = 987654321                   # 계산해주고 (edge case를 처리하는 경우에 up/left 둘 중 하나만 구해지는 경우를 대비한 초기화)
                                            # 2가지 경우만 있음: 위에서 오는 경우, 왼쪽에서 오는 경우
    if r != 0:                              # (edge case 제거 -> 0열 -> 제외)
        up = solve(r-1, c)                  # 위에서 오는 경우의 값을 얻어오고
    if c != 0:                              # (edge case 제거 -> 0행 -> 제외)
        left = solve(r, c-1)                # 왼쪽에서 오는 경우의 값을 얻어와야 한다.

    # 3. 계산해서 저장하고 반환
    memo[r][c] = min(up, left) + arr[r][c]  # 왼쪽 / 위에서 온 경우 중 최솟값과 현재 위치의 값을 계산 후 저장
    return memo[r][c]

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 987654321
    memo = [[-1] * N for _ in range(N)]             # 초기값 -1이 의미하는 것은 해당 위치의 문제의 해를 구하지 않았음을 표현
    ans = solve(N-1, N-1)                           # 마지막에서 시작
    print('#{} {}'.format(tc, ans))