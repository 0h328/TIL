import sys
sys.stdin = open('input.txt')

pattern = {(2, 1, 1): 0,
           (2, 2, 1): 1,
           (1, 2, 2): 2,
           (4, 1, 1): 3,
           (1, 3, 2): 4,
           (2, 3, 1): 5,
           (1, 1, 4): 6,
           (3, 1, 2): 7,
           (2, 1, 3): 8,
           (1, 1, 2): 9
           }

hexTobin = {'0': [0, 0, 0, 0], '1': [0, 0, 0, 1], '2': [0, 0, 1, 0], '3': [0, 0, 1, 1], '4': [0, 1, 0, 0],
            '5': [0, 1, 0, 1], '6': [0, 1, 1, 0], '7': [0, 1, 1, 1], '8': [1, 0, 0, 0],
            '9': [1, 0, 0, 1], 'A': [1, 0, 1, 0], 'B': [1, 0, 1, 1], 'C': [1, 1, 0, 0], 'D': [1, 1, 0, 1],
            'E': [1, 1, 1, 0], 'F': [1, 1, 1, 1]}


def find_start():
    ans = 0
    for i in range(N):
        j = M * 4 - 1

        while j >= 55:
            if bin_data[i][j] and bin_data[i - 1][j] == 0:
                pw = []
                for _ in range(8):
                    a=b=c=0
                    while bin_data[i][j] == 0:
                        j -= 1
                    while bin_data[i][j] == 1:
                        c += 1
                        j -= 1
                    while bin_data[i][j] == 0:
                        b += 1
                        j -= 1
                    while bin_data[i][j] == 1:
                        a += 1
                        j -= 1
                    pw.append(pattern[(a,b,c)])


                b = pw[0] + pw[2] + pw[4] + pw[6]
                a = pw[1] + pw[3] + pw[5] + pw[7]

                if (a * 3 + b) % 10 == 0:
                    ans += a + b

            j -= 1

    return ans


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    bin_data = [[] for _ in range(N)]

    for i in range(N):
        tmp = input()
        for j in range(M):
            bin_data[i] += hexTobin[tmp[j]]

    print("#{} {}".format(tc, find_start()))