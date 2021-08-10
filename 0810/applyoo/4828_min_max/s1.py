import sys
sys.stdin = open('input.txt')

def min_max(arr):
    maxi = mini = arr[0]

    for i in arr:
        if i > maxi:
            maxi = i
        elif i < mini:
            mini = i

    return maxi - mini

T = int(input())

for i in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    print('#{} {}'.format(i+1, min_max(arr)))