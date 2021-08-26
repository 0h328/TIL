import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split()) #숫자 개수, 작업 횟수
    nums = list(map(int, input().split()))

    for _ in range(M):
        nums.append(nums.pop(0))

    print('#{} {}'.format(t, nums[0]))