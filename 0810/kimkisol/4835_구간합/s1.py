import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    min_sum = max_sum = temp = sum(nums[:M]) #첫구간 합
    #1번째 인덱스부터 마지막 구간 시작지점까지
    for idx in range(1, len(nums)-M+1): #현재 인덱스 = 구간의 시작지점
        #이전 구간의 맨왼쪽값은 빼고 새로운 오른쪽 값 추가
        temp = temp - nums[idx-1] + nums[idx+M-1]
        if temp > max_sum:
            max_sum = temp
        if temp < min_sum:
            min_sum = temp
    result = max_sum - min_sum

    print('#{} {}'.format(t, result))