def solve(N, numbers):
    result = []
    # numbers.sort()
    for i in range(N-1, 0, -1): # 버블
        for j in range(i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    # 앞/뒤 5개씩 (총 10개)
    for i in range(1, 6):
        # 가장 큰 값(정렬 기준 제일 뒤)
        result.append(numbers[-i])
        # 가장 다음 값(정렬 기준 제일 앞)
        result.append(numbers[i-1])
    return ' '.join(map(str, result))

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    ans = solve(N, numbers)
    print('#{} {}'.format(tc, ans))