import sys
sys.stdin = open('input.txt')

for k in range(1, 11):   # 총 10개의 tc
    N = int(input())
    numbers = list(map(int, input(). split()))
    cnt = 0
    for i in range(2, N - 2):
        if numbers[i] > numbers[i - 2] and numbers[i] > numbers[i - 1] and numbers[i] > numbers[i + 1] and numbers[i] > numbers[i + 2]:
            data = [numbers[i - 2], numbers[i - 1], numbers[i + 1], numbers[i + 2]]
            max_data = data[0]
            for j in range(4):
                if data[j] > max_data:
                    max_data = data[j]
                    j += 1
            # max_data = max(numbers[i-2], numbers[i-1], numbers[i+1], numbers[i+2])
            cnt += numbers[i] - max_data
        else:
            continue
    print("#{} {}".format(k, cnt))