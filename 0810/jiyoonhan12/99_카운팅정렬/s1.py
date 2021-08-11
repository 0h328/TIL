import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(T):
    arr = list(map(int, input().split()))

    def counting_sort(arr):

        new_arr = [0] * len(arr)
        count = [0] * (max(arr) + 1)

        for i in range(len(arr)):
            count[arr[i]] += 1

        for i in range(len(count) - 1):
            count[i+1] += count[i]

        for i in range(len(arr) - 1, -1, -1):
            new_arr[count[arr[i]] - 1] = arr[i] # 새 리스트의 인덱스로 들어갈 때는 -1 해줘야 함
            count[arr[i]] -= 1

        return new_arr

    max_num = max(arr)
    print(counting_sort(arr))