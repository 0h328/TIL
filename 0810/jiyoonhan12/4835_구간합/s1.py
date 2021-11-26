import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):

    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    list_sum = []
    for n in range(N - M + 1): # 구간합 더한 리스트 만들기
        sum_num = 0
        for m in range(M):
            sum_num += numbers[n+m]
        list_sum.append(sum_num)

    def bubble(arr):  # 버블정렬 (항목 개수가 많지 않을 때)
        for i in range(len(arr) - 1, 0, -1):
            for j in range(i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

    bubble(list_sum)
    sub = list_sum[len(list_sum) -1] - list_sum[0]
    print('#{} {}'.format(t, sub))