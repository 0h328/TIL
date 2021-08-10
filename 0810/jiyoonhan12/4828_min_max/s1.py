import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):

    case = int(input())
    numbers = list(map(int, input().split()))

    def bubble(arr): # 버블정렬 (항목 개수가 많지 않아서 유용)
        for i in range(len(arr)-1, 0, -1):
            for j in range(i):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

    bubble(numbers) # 리스트 정렬 후
    sub = numbers[len(numbers) - 1] - numbers[0] # 마지막 항목 - 첫 번째 항목
    print('#{} {}'.format(t, sub))