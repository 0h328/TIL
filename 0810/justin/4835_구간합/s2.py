import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())            # N: 원소의 개수 / M: 구간의 길이
    numbers = list(map(int, input().split()))

    max_value = 0                               # 최대 & 최소 초깃값 설정
    min_value = 987654321

    for i in range(N-M+1):                      # 구간 길이(N-M+1)
        tmp = 0
        for j in numbers[i:i + M]:              # 슬라이싱 연산의 비효율성
            tmp += j

        if max_value < tmp:
            max_value = tmp
        if min_value > tmp:
            min_value = tmp
    ans = max_value - min_value
    print('#{} {}'.format(tc, ans))