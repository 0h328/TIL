import sys
sys.stdin = open('input.txt')

test_case = int(input())

for tc in range(1, test_case+1):
    num, section = map(int, input().split())
    num_list = list(map(int, input().split()))
    max_sum = 0                         # 합의 최댓값
    min_sum = 10**10                    # 합의 최솟값

    for i in range(num-section+1):      # 구역의 첫번째 인덱스, 마지막 구역의 첫 인덱스는 (리스트길이 - 구역길이 + 1)
        tmp_sum = 0                     # 하나의 구역에서의 합 결과를 저장할 임시변수
        for j in range(i, i+section):   # 구역의 첫 인덱스부터 구역의 마지막의 인덱스까지 순환
            tmp_sum += num_list[j]

        if max_sum < tmp_sum:           # 기존보다 크거나 작은 합이 있으면 새로 저장
            max_sum = tmp_sum
        if min_sum > tmp_sum:
            min_sum = tmp_sum

    answer = max_sum - min_sum

    print('#{} {}'.format(tc, answer))