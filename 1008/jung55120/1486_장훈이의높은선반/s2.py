# 성렬님 코드 참고

import sys
sys.stdin = open('input.txt')

def dfs(idx, total):
    global min_height
    if total >= min_height:
        return

    if idx == N:
        if B <= total < min_height:
            min_height = total  # 가지치기 생각해보기
        return

    dfs(idx+1, total)
    dfs(idx+1, total+height[idx])

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split()) # N은 점원의 수, B는 선반의 높이
    height = list(map(int, input().split()))
    min_height = 200000
    dfs(0, 0)
    print('#{} {}'.format(tc, min_height-B))


