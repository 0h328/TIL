import sys
sys.stdin = open('input.txt')


asc = [[0, 0, 0, 0],  #0
       [0, 0, 0, 1],  #1
       [0, 0, 1, 0],  #2
       [0, 0, 1, 1],  #3
       [0, 1, 0, 0],  #4
       [0, 1, 0, 1],  #5
       [0, 1, 1, 0],  #6
       [0, 1, 1, 1],  #7
       [1, 0, 0, 0],  #8
       [1, 0, 0, 1],  #9
       [1, 0, 1, 0],  #A
       [1, 0, 1, 1],  #B
       [1, 1, 0, 0],  #C
       [1, 1, 0, 1],  #D
       [1, 1, 1, 0],  #E
       [1, 1, 1, 1]]  #F


def find_pos(arr, N, M):
    # if (N, M) == (100, 26):
    #     pos_cnt = 1
    # elif (N, M) == (200, 50):
    #     pos_cnt = 2
    # elif (N, M) == (500, 126):
    #     pos_cnt = 5
    pos = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] != '0':
                pos.append(arr[i][j])
        if pos and arr[i][j] == '0':
            pos.append('*')
    return pos


T = int(input())
for tc in range(1, 2):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    pos = find_pos(arr, N, M)
    x = ''

    for i in pos:
        if i == '*':
            last_chr_idx = i

    for i in range(last_chr_idx+1):
        x.append(asc[pos[i]])






