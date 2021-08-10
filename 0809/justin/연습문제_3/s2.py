def solve(N, blocks):
    max_drop = 0                  # 낙차가 가장 큰 값

    for i in range(N-1):          # 마지막 박스는 움직일 수 없기 때문에 N-1 제외하고 반복
        cur_block = blocks[i]     # 현재 위치한 블럭
        parts = blocks[i+1:]      # i 다음에 있는 나머지 요소
        drop = 0                  # 낙차의 크기 기록

        for idx in range(len(parts)):   # 오른쪽 돌면서
            if cur_block > parts[idx]:  # 현재보다 작은 상자의 개수 카운트 (같아도 안되는 이유? 떨어질 때 거기서 하나 걸리기 때문에)
                drop += 1               # 낙차 1 증가
        if max_drop < drop:             # 최종 낙차의 크기가 구해지면 그 중에서 최댓값 구하기
            max_drop = drop
    return max_drop

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())                          # 정사각형의 길이
    blocks = list(map(int, input().split()))  # 상자의 길이가 담겨 있는 배열
    ans = solve(N, blocks)
    print('#{} {}'.format(tc, ans))