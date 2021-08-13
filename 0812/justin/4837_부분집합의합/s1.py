import sys
sys.stdin = open('input.txt')
T = int(input())
nums = range(1, 13)
for tc in range(1, T+1):                # 1 ~ 12 준비 -> 1 ~ 12까지의 숫자를 원소로 가진 집합 A
    N, K = map(int, input().split())    # N: 부분집합의 개수 / K: N개의 부분집합 요소로 만드는 합
    ans = 0                             # 최종 결과 (가짓수)
    for i in range(1 << len(nums)):     # 1부터 2^12(len(nums)까지 전부 확인 -> 모든 부분집합의 가짓수 확인
        total = 0                       # total -> N개의 부분집합의 합
        cnt = 0                         # 부분집합의 개수 count
        for j in range(len(nums)):
            if i & (1 << j):
                total += nums[j]        # 그때의 그 값을 total에 더하고
                cnt += 1                # 부분집합의 개수 cnt

        if cnt == N and total == K:     # cnt가 N개이고 그때의 합이 K인 경우만
            ans += 1                    # 1 증가

    print('#{} {}'.format(tc, ans))