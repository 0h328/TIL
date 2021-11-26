import sys
sys.stdin = open('input.txt')

def binary_search(arr, left, right, target, left_check=False, right_check=False):
    if left > right:
        return False

    mid = (left+right)//2
    if arr[mid] == target:
        return True
    elif arr[mid] < target:
        if left_check==False and right_check==False:
            return binary_search(arr, mid+1, right, target, left_check=left_check, right_check=True)
        if left_check:
            return binary_search(arr, mid+1, right, target, left_check=False, right_check=True)
        return False
    else:
        if left_check==False and right_check==False:
            return binary_search(arr, left, mid-1, target, left_check=True, right_check=False)
        if right_check:
            return binary_search(arr, mid+1, right, target, left_check=True, right_check=False)
        return False

for T in range(int(input())):
    result = 0
    N, M = map(int, input().split())

    lst = sorted(list(map(int, input().split())))
    targets = list(map(int, input().split()))

    for t in targets:
        result+=binary_search(lst, 0, N-1, t)
    
    print('#{} {}'.format((T+1), result))

#1 2
#2 0
#3 3