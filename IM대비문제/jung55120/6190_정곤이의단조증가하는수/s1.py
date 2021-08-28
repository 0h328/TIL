import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    stack = []
    cnt = 0
    while cnt < N:
        for i in range(N - cnt):
            for j in range(i + 1, N):
                stack.append(numbers[i] * numbers[j])
            cnt += 1

    for i in range(len(stack)):
        check = stack.pop()
        check_str = list(str(check))
        result = 0
        for j in range(1, len(check_str)):
            if check_str[j] > check_str[j-1]:
                pass
            else:
                result = -1
                break
        if result == 0 and len(check_str) > 1:
            result = check
            break


    print('#{} {}'.format(tc, result))