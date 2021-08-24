# 선택 정렬

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(len(a)-1):                   # 마지막 요소와 비교하기 위해
        min_num = i                             # 첫번째 인덱스로 변수 설정
        for j in range(i+1, len(a)):            # 첫번째 인덱스에 해당하는 요소와 비교하기 위해
            if a[min_num] > a[j]:
                min_num = j
        a[i], a[min_num] = a[min_num], a[i]

    print('#{}'.format(tc), end=' ')
    print(*a)


