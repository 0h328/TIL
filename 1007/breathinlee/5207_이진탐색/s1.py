import sys
sys.stdin = open('input.txt')

# M_numbers에 저장된 M개의 정수에 대해 N_numbers에 들어있는 수인지 확인

def binary_search(numbers, target, start, end):
    global cnt
    while start <= end:
        mid = start + (end - start)//2
        if numbers[mid] == target:
            cnt += 1
            return 1
        elif numbers[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    N_numbers = sorted(list(map(int, input().split())))
    M_numbers = list(map(int, input().split()))

    start = 0
    end = N - 1
    cnt = 0
    for i in range(M):
        target = M_numbers[i]
        result = binary_search(N_numbers, target, start, end)

    print('#{} {}'.format(tc, cnt))

