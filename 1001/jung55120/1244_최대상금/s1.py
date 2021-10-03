import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    money, times = input().split()
    money = list(map(int, money))
    times = int(times)
    print('{}번째 입니다'.format(tc))
    for time in range(1, times+1):
        max_num_index = 0
        for i in range(time, len(money)):
            if money[time-1] < money[i]:
                max_num_index = i
        money[time-1], money[max_num_index] = money[max_num_index], money[time-1]
    print(money)