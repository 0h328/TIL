import sys
sys.stdin = open('input.txt')

# 미완성

# M_numbers에 저장된 M개의 정수에 대해 N_numbers에 들어있는 수인지 확인
# 동시에 탐색 과정에서 양쪽구간을 번갈아 선택하게 되는 숫자의 개수

def binary_search(target, start, end):
    global cnt
    while start <= end:
        mid = start + (end - start) // 2
        if N_numbers[mid] == target:
            if (visited[0] == 0 and visited[1] == 1) or (visited[0] == 1 and visited[1] == 0):
                break
            cnt += 1
            return
        elif N_numbers[mid] < target:
            start = mid + 1
            visited[1] = 1
        else:
            end = mid - 1
            visited[0] = 1
    return -1



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    N_numbers = sorted(list(map(int, input().split())))
    M_numbers = list(map(int, input().split()))
    visited = [0, 0]   # left, right 들렸는지 확인
    cnt = 0

    for i in range(M):
        target = M_numbers[i]
        visited = [0, 0]
        result = binary_search(target, 0, N-1)

    print('#{} {}'.format(tc, cnt))