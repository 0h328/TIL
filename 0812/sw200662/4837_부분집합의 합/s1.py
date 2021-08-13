import sys

sys.stdin = open('input.txt')

T = int(input())

for k in range(T):
    N, K = map(int, input().split())
    list1 = []
    cnt = 0 # 몇개나 있는지 확인
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    for i in range(1 << len(nums)):
        a = []
        for j in range(len(nums)):
            if i & (1 << j):
                a.append(nums[j]) # 모든 부분집합을 우선 생성

        if len(a) == N and sum(a) == K: #모든 부분집합에서 N개의 갯수를 가지고, 합이 K개인것을 확인
            cnt += 1 # 조건에 만족하는것에 있다면 cnt += 1
    print('#{} {}'.format(k + 1, cnt))
