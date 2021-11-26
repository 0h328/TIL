# 카운팅 정렬

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    a = list(map(int, input().split()))

    cnt = [0] * (max(a) + 1)
    temp = [0] * n

    for i in range(n):
        cnt[a[i]] += 1
    # print('입력 받은 원소를 인덱스로 바꾼 list :',cnt)

    for i in range(1, len(cnt)):
        cnt[i] += cnt[i-1]
    # print('각 항목에 위치할 개수를 반영하기 위해 누적한 list :',cnt)

    for i in range(n):
        cnt[a[i]] -= 1              # 빼지 않으면 IndexError 발생
        temp[cnt[a[i]]] = a[i]
    # print(temp)

    print('#{}'.format(tc), end=' ')
    print(*temp)