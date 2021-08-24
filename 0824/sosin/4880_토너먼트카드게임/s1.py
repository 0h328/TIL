import pathlib, sys
sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + '/input.txt')

def check_winner(a, b):
    if abs(a-b) == 1:
        return max(a, b)
    else: 
        return min(a, b)

def binary_rcp(arr, start, end):
    if len(arr) == 1: 
        return (arr[0], start)
    elif len(arr) == 2: 
        return (arr[0], start) if check_winner(arr[0], arr[1]) == arr[0] else (arr[1], end)
    else:
        mid = (len(arr)-1)//2
        mid_idx = (start+end)//2
        a, left_idx = binary_rcp(arr[:mid+1], start, mid_idx)
        b, right_idx = binary_rcp(arr[mid+1:], mid_idx+1, end)
        return (a, left_idx) if check_winner(a, b) == a else (b, right_idx)

for T in range(int(input())):
    N = int(input())
    students = list(map(int, input().split()))
    a, winner_idx = binary_rcp(students, 0, len(students)-1)
    print('#{} {}'.format((T+1), winner_idx+1))

#1 3
#2 5
#3 1
