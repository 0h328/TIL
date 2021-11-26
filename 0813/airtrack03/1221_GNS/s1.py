# 카운팅 정렬 풀이 방식

import sys
sys.stdin = open('input.txt')

# 각 문자를 인덱스로 접근하기 위해 리스트를 만들어주고 인덱스는 .index() 통해 접근
num_list = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

T = int(input())

for tc in range(1, T+1):
    N = int(input().split()[1])     # 테스트 케이스 길이
    cnt = [0] * 10      # 각 문자를 카운팅할 리스트
    ans = [0] * N       # 정렬된 순서로 문자 입력할 리스트

    data = input().split()

    for i in range(N):      # 문자 개수 카운팅
        cnt[num_list.index(data[i])] += 1

    for i in range(1, len(cnt)):    # 카운팅된 거 누적으로 변환
        cnt[i] += cnt[i-1]

    for i in range(N-1, -1, -1):    # 끝 문자부터 해당하는 인덱스에 입력
        ans[cnt[num_list.index(data[i])] - 1] = data[i]
        cnt[num_list.index(data[i])] -= 1

    print('#{}'.format(tc))
    print(' '.join(list(map(str, ans))))