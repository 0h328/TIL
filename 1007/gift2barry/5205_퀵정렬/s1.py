import sys
sys.stdin = open('input.txt')

'''
총 소요시간: 1시간 15분
디버깅: 20분
'''

def partition(tmp, l, r):
    p = tmp[l]
    i, j = l, r
    while i <= j:
        while i <= j and tmp[i] <= p:
            i += 1
        while i <= j and tmp[j] >= p:
            j -= 1
        if i < j:
            tmp[i], tmp[j] = tmp[j], tmp[i]

    tmp[l], tmp[j] = tmp[j], tmp[l]
    return j


def quick(arr, lp, rp):

    if lp < rp:
        pivot = partition(arr, lp, rp)
        quick(arr, lp, pivot-1)
        quick(arr, pivot+1, rp)


for tc in range(1, int(input())+1):

    N = int(input())
    nums = list(map(int, input().split()))
    left_pivot = 0
    right_pivot = N-1
    quick(nums, left_pivot, right_pivot)
    print('#{} {}'.format(tc, nums[N//2]))