import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def BinarySearch(left, right, target):
    cnt = 0
    while left <= right:
        cnt += 1
        center = int((left + right) / 2)
        if target > center:
            left = center
        elif target < center:
            right = center
        else:
            return cnt

T = int(input())

for t in range(1, T+1):
    P, A, B = map(int, input().split())
    if BinarySearch(1, P, A) < BinarySearch(1, P, B):
        result = 'A'
    elif BinarySearch(1, P, A) > BinarySearch(1, P, B):
        result = 'B'
    else:
        result = 0
    print('#{} {}'.format(t, result))
