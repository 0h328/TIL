import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    nums = list(range(1, 13))
    result = 0

    #전체 부분집합 경우의 수
    for i in range(1<<12):
        cnt_nums = 0
        sum_nums = 0
        #0~11까지 nums idx
        for j in range(12):
            #부분 집합 요소개수가 N보다 크거나 합이 K보다 크면 break
            if cnt_nums > N or sum_nums > K:
                break
            #0번째 자리에 숫자가 있는지 확인
            if i & (1<<j):
                sum_nums += nums[j]
                cnt_nums += 1
        #전체 다 돌고 부분 집합 요소개수랑 합이 각각 N, K와 같으면 result +1
        if cnt_nums == N and sum_nums == K:
            result += 1

    print('#{} {}'.format(t, result))

