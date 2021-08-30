import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    stack = []
    result = -1

    for i in range(N):
        for j in range(i + 1, N):
            check = 0
            num = numbers[i] * numbers[j]
            num_str = str(num)
            # print(num_str)

            for k in range(1, len(num_str)):
                if num_str[k] < num_str[k - 1]:
                    check = -1
                    break
            if check != -1 and num > result:
                result = num

    print('#{} {}'.format(tc, result))