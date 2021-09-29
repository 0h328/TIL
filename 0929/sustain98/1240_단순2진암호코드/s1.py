import sys
sys.stdin = open('input.txt')

t = int(input())
val = {'0001101': 0, '0011001': 1, '0010011': 2,
       '0111101': 3, '0100011': 4, '0110001': 5,
       '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9
       }
for idx in range(1, t+1):
    n, m = map(int, input().split())

    res = 0
    for i in range(n):
        line = input()
        if '1' in line:
            last_idx = line.rfind('1') + 1
            l = []
            for j in range(8):
                l.append(val[line[last_idx - (j+1)*7:last_idx - j*7]])
            if (sum(l) + (l[7] + l[5] + l[3] + l[1]) * 2) % 10 == 0:
                res = sum(l)
                for _ in range(i+1, n):
                    input()
                break
    print('#{} {}'.format(idx, res))
