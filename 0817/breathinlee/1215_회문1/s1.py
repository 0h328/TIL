import sys
sys.stdin = open("input.txt")

for tc in range(1, 11):
    M = int(input())                      # 회문의 길이
    arr = [input() for _ in range(8)]
    ret1 = 0
    ret2 = 0

    # 행 고려
    for i in range(8):
        for j in range(8-M+1):
            for k in range(M//2):
                if arr[i][j+k] != arr[i][j+M-1-k]:
                    break
            else:
                ret1 += 1

    # 열 고려
    for i in range(8):
        for j in range(8-M+1):
            for k in range(M//2):
                if arr[j+k][i] != arr[j+M-1-k][i]:
                    break
            else:
                ret2 += 1


    print('#{} {}'.format(tc, ret1+ret2))