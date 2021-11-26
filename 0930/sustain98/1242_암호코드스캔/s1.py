import sys
sys.stdin = open('input.txt')


t = int(input())
val = {'0001101': 0, '0011001': 1, '0010011': 2,
       '0111101': 3, '0100011': 4, '0110001': 5,
       '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9
       }

def find_code():
    for line in codes:
        if line:
            line = '0' + line
            bin_line = ''
            for k in line:
                bin_line += ('0000' + str(bin(int(k, 16)))[2:])[-4:]

            last_idx = bin_line.rfind('1') + 1
            bin_line = bin_line[:last_idx]
            count = [0] * 4
            i = 3
            start = last_idx - 1
            j = start
            print(bin_line)
            while i > -1:
                if bin_line[j] != bin_line[j - 1]:
                    count[i] = start - j + 1
                    i -= 1
                    start = j-1
                j -= 1
            ratio = sum(count) // 7

            if last_idx >= 8*7*ratio:
                bin_line = bin_line[last_idx % 56:]
            else:
                bin_line = ('0'*(8*7*ratio - len(bin_line)) + bin_line)
            print(ratio, bin_line, len(bin_line))
            line = ''
            for k in range(0, 56*ratio, ratio):
                line += bin_line[k]
            print(line)
            l = []
            for j in range(8):
                l.append(val[line[j * 7:(j+1) * 7]])
            print(l, sum(l) + (l[7] + l[5] + l[3] + l[1]) * 2)
            if (sum(l) + (l[7] + l[5] + l[3] + l[1]) * 2) % 10 == 0:
                return sum(l)
    return 0

for idx in range(1, t+1):
    n, m = map(int, input().split())
    codes = set()
    for _ in range(n):
        codes |= set(input().replace('0', '').split())
    print(codes)
    res = find_code()
    print('#{} {}'.format(idx, res))