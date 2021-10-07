import sys
sys.stdin = open('input.txt')

T = int(input())

def pivot_select(arr,start,end):
    pivot = arr[start]
    left = start + 1
    right = end
    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and pivot <= arr[right]:
            right -= 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[start], arr[right] = arr[right], arr[start]
    return right


def quick_sort(arr,start,end):
    if start < end:
        pivot = pivot_select(arr, start, end)
        quick_sort(arr, start, pivot - 1)
        quick_sort(arr, pivot + 1, end)
    return arr

for tc in range(1,T+1):
    N = int(input())
    list_num = list(map(int,input().split()))
    ans = quick_sort(list_num,0,len(list_num)-1)
    print('#{} {}'.format(tc,ans[len(ans)//2]))
