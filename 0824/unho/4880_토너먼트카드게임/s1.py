'''
분할정복
'''

import sys
sys.stdin = open('input.txt')


'''
def solution(idx, length):   # idx - 시작 인덱스 / length - 길이
    #Base Case
    if length == 2:
        if n_list[idx] - n_list[idx+1] == -1 or n_list[idx] - n_list[idx+1] == 2:
            return idx+1
        return idx
    elif length == 1:
        return idx

    solution(idx, length//2), solution(idx+length//2, length//2)
'''

def solution(arr):
    #Base Case
    if len(arr) == 2:
        if arr[0][1] - arr[1][1] == -1 or arr[0][1] - arr[1][1] == 2:
            return [arr[1]]
        return [arr[0]]
    elif len(arr) == 1:
        return [arr[0]]

    next = ((len(arr)-1)//2)+1
    return solution(solution(arr[:next]) + solution(arr[next:]))



test_case = int(input())

for tc in range(1, test_case+1):
    N = int(input())
    n_list = list(enumerate(map(int, input().split()), start=1))

    answer = solution(n_list)

    print('#{} {}'.format(tc, answer[0][0]))