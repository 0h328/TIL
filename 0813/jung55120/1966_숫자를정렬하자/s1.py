import sys
sys.stdin = open('input.txt')

TC = int(input())
for tc in range(1, TC+1):
    cnt = int(input())
    numbers = list(map(int, input().split()))

    # 가장 쉬운 방법
    # numbers.sort()
    # number = ' '.join(str(_) for _ in numbers)
    #
    # print('#{} {}'.format(tc, number))

    for i in range(cnt-1):
        for j in range(cnt-i):
            if numbers[i] > numbers[i+j]:
                numbers[i], numbers[i+j] = numbers[i+j], numbers[i]

    number = ' '.join(str(_) for _ in numbers)

    print('#{} {}'.format(tc, number))
