import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    L = list(map(int, input().split()))

    def binary_search(numbers, target):
        start = 1
        end = numbers
        cnt = 0
        while start <= end:
            cnt += 1
            middle = int((start + end) / 2)
            if middle == target:
                return cnt
            elif middle > target:
                end = middle
            else:
                start = middle
        return numbers  # 요기좀 이상한데 일단 통과하겠습니다. (되네?)

    if binary_search(L[0], L[1]) > binary_search(L[0], L[2]):
        print('#{} {}'.format(tc + 1, 'B'))
    elif binary_search(L[0], L[1]) < binary_search(L[0], L[2]):
        print('#{} {}'.format(tc + 1, 'A'))
    else:
        print('#{} {}'.format(tc + 1, '0'))