import sys
sys.stdin = open('input.txt')

for a in range(10):
    N = int(input())
    arr = list(map(int, input().split()))
    total = 0

    for j in range(2, N-2):
        if arr[j] > max(arr[j-2], arr[j-1], arr[j+1], arr[j+2]):
            total += (arr[j] - max(arr[j-2], arr[j-1], arr[j+1], arr[j+2]))

    print('#{} {}'.format(a+1, total))

# i는 2 ~ N - 3
# i - 2, i - 1, i + 1, i + 2
# i가 제일 클 때, 주변의 4개 중 젤 큰놈이 필요!(max)
# 빼면 조망권 확보한 층!