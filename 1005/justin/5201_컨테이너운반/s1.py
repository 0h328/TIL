"""
Greedy
- 순간의 선택에 집중
- 정렬 시켜 놓고 컨테이너를 화물에 실을 수 있는지 여부 판단
"""

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())        # N: 컨테이너, M: 트럭
    w = list(map(int, input().split()))     # 컨테이너의 무게
    t = list(map(int, input().split()))     # 트럭의 적재용량
    w.sort(reverse=True)                    # 역순으로 정렬
    t.sort(reverse=True)
    i = j = ans = 0                         # i & j는 w와 t에서 활용되는 인덱스 / ans는 컨테이너의 개수 누적

    while i <= N-1 and j <= M-1:            # 인덱스를 기준으로 삼을 때는 (기본적으로) N-1 / M-1이 끝 값
        if w[i] <= t[j]:                    # 컨테이너의 무게가 적재 용량보다 작거나 같은 경우
            ans += w[i]                     # 무게 누적
            i, j = i+1, j+1                 # 다음 작업 처리 (i와 j가 N-1과 M-1이 될때까지)
        else:                               # 실을 수 없는 경우
            i += 1                          # i 증가-> 해당 컨테이너는 실을 수 없으니까 이동 / j는 다음 컨테이너의 무게를 봐야 하기 때문에 그대로
    print('#{} {}'.format(tc, ans))