import sys
sys.stdin = open('input.txt')

for tc in range(10):
    N = int(input())
    arr = list(map(int, input().split()))
    decrease = [1, 2, 3, 4, 5]            # 감소하는 싸이클
    i = 0

    while True:
        i %= 5                            # 싸이클 반복
        value = arr.pop(0) - decrease[i]
        arr.append(value)
        if value <= 0:
            arr[-1] = 0
            break
        i += 1

    print('#{}'.format(N), end=' ')
    print(*arr)

    # while True:
    #     i %= 5
    #     value = arr.pop(0) - decrease[i]
    #     if value > 0:
    #         arr.append(value)
    #     else:
    #         arr[-1] = 0
    #         break
    #     i += 1
