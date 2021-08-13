# 엣지케이스 보완 필요!!!!!! 10개 중 9개만 통과됨..

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    for i in range(0, len(numbers)-1, 2):       # 짝수번째 인덱스에는 최댓값 순으로 정렬
        max_idx = i
        for j in range(i+1, len(numbers)):
            if numbers[max_idx] < numbers[j]:
                max_idx = j
        numbers[i], numbers[max_idx] = numbers[max_idx], numbers[i]

    for i in range(1, len(numbers), 2):         # 홀수번째 인덱스에는 최솟값 순으로 정렬
        min_idx = i
        for j in range(i+1, len(numbers)):
            if numbers[min_idx] > numbers[j]:
                min_idx = j
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

    print('#{}'.format(tc), end=' ')
    for k in range(10):
        print(numbers[k], end=' ')
    print()