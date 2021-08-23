import sys
sys.stdin = open('input.txt')

T = int(input())

def rotate(data):
    res = []
    for i in range(len(data)):
        pre = []
        for j in range(len(data)-1, -1, -1):
            pre.append(data[j][i])
        res.append(pre)
    return res

for case in range(T):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]
    data_90 = rotate(data)
    data_180 = rotate(data_90)
    data_270 = rotate(data_180)
    print('#{}'.format(case + 1))
    for i in range(N):
        print(''.join(map(str,data_90[i])), end =' ')
        print(''.join(map(str, data_180[i])), end=' ')
        print(''.join(map(str, data_270[i])), end=' ')
        print()

