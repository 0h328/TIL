'''
다시 풀어보기
'''

import sys
sys.stdin = open('input.txt')


def solution(start, end):
    #Base Case
    if start == end:
        return start

    left = solution(start, (start + end) // 2)
    right = solution((start + end) // 2 + 1, end)

    if arr[right] - arr[left] == 1 or arr[right] - arr[left] == -2:
        return right
    return left





test_case = int(input())

for tc in range(1, test_case+1):
    N = int(input())
    arr = [0] + list(map(int, input().split()))

    answer = solution(1, N)
    print('#{} {}'.format(tc, answer))