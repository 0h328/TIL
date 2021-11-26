import sys

sys.stdin = open('input.txt')


def rotation(data):
    result = []
    for i in range(N):
        tmp = []
        for j in range(N - 1, -1, -1):
            tmp.append(data[j][i])
        result.append(tmp)
    return result

def rotate(key):
    return list(zip(*key[::-1]))

for test in range(1, 1 + int(input())):
    N = int(input())

    data = [input().split() for _ in range(N)]

    deg_90 = rotate(data)

    deg_180 = rotate(deg_90)

    deg_270 = rotate(deg_180)
    print('#{}'.format(test))
    for i in range(N):
        print(''.join(deg_90[i]), ''.join(deg_180[i]), ''.join(deg_270[i]))
