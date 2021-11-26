import sys
sys.stdin = open('input.txt')

def counting(arr):
    sort_list = [0] * len(arr)
    cnt_list = [0] * (max(arr) + 1)

    for i in range(len(arr)):
        cnt_list[arr[i]] += 1

    for i in range(len(cnt_list)-1):
        cnt_list[i+1] += cnt_list[i]

    for i in range(len(arr)):
        sort_list[cnt_list[arr[i]] - 1] = arr[i]
        cnt_list[arr[i]] -= 1

    return sort_list

T = int(input())

for tc in range(T):
    arr = list(map(int, input().split()))

    print(counting(arr))