import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    sum_list = []
    i = 0
    while True:
        my_sum = sum(numbers[i:i+M])
        sum_list.append(my_sum)
        i += 1
        if i > N - M:
            break
    max_value = max(sum_list)
    min_value = min(sum_list)

    print('#{} {}'.format(tc, max_value - min_value))
