import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    for i in range(len(numbers)-1, 0, -1):            # 버블정렬 사용
        for j in range(i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    print('#{}'.format(tc), end=' ')
    print(*numbers)
