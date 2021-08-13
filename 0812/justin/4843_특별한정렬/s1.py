def solve(data):
    for i in range(10):  # 10개의 구간까지 정렬
        min_idx = i
        if i % 2 == 0:   # 구간의 시작이 짝수인 경우 최대값
            for j in range(i+1, N):
                if data[min_idx] < data[j]:
                    min_idx = j
        else:
            for j in range(i+1, N):
                if data[min_idx] > data[j]:
                    min_idx = j
        # t = data[i]            			# 구간의 맨 앞에 최대나 최소를 가져옴
        # data[i] = data[mIdx]
        # data[mIdx] = t
        data[i], data[min_idx] = data[min_idx], data[i]

    return

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    solve(data)
    print('#{}'.format(tc), end=' ')
    for i in range(10):
        print(data[i], end=' ')
    print()