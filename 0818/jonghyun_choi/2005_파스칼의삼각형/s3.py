import sys
sys.stdin = open('input.txt')

T = int(input())

def pascal(num):
    res = []
    for cnt in range(1, num + 1):
        res.append([1]*cnt)

    for i in range(1, num):
        for j in range(1, len(res[i])-1):
            res[i][j] = res[i-1][j-1] + res[i-1][j]

    return res

for case in range(T):
    N = int(input())

    print('#{}'.format(N))

    for i in pascal(N):
        for j in i:
            print(j, end=' ')
        print()