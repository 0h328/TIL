import sys
sys.stdin = open('input.txt')

T = int(input())

def win(A, B):
    if (A == 1 and B == 3) or (A == 2 and B == 1) or (A == 3 and B == 2):
        return 0
    elif A == B:
        return 0
    else:
        return 1

def merge_sort(data):
    if len(data) == 1:
        return data[0]
    if len(data) == 2:
        return data[win(data[0], data[1])]

    mid = (len(data) // 2) if len(data) % 2 == 0 else (len(data) // 2) + 1
    low_data = merge_sort(data[:mid])
    high_data = merge_sort(data[mid:])

    winner = win(low_data, high_data)

    if winner == 0:
        return low_data
    else:
        return high_data



for case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    print('#{} {}'.format(case + 1, merge_sort(data)))
