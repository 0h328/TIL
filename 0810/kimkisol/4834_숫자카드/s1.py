import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())

for t in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().rstrip()))
    cnt = [0] * 10
    #숫자 개수를 cnt리스트에 저장
    for num in nums:
        cnt[num] += 1
    max_cnt = 0
    max_idx = 0
    #cnt리스트에서 가장 큰값과 그 값의 idx 구하기
    for idx, num_cnt in enumerate(cnt):
        if num_cnt >= max_cnt:
            max_cnt = num_cnt
            max_idx = idx
    print('#{} {} {}'.format(t, max_idx, max_cnt))