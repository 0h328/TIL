import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    print(arr)

    # [[1, 2, 3],
    #  [4, 5, 6],
    #  [7, 8, 9]]



