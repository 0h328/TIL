import sys
sys.stdin = open('input.txt')


t = int(input())
val = {'0001101': 0, '0011001': 1, '0010011': 2,
       '0111101': 3, '0100011': 4, '0110001': 5,
       '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9
       }

def find_code():
    for i in range(n):
        line = input().strip('0')
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
                bin_line = '0'*(8*7*ratio) + bin_line

            line = ''

            if ratio > 1:
                line = ''
                for k in range(len(bin_line)-1, -1, -1*ratio):
                    # print(k)
                    line = bin_line[k] + line
                bin_line = line

            print(bin_line)
            l = []
            for j in range(8):
                l.append(val[bin_line[j * 7:(j+1) * 7]])
            print(l)
            if (sum(l) + (l[7] + l[5] + l[3] + l[1]) * 2) % 10 == 0:
                for _ in range(i+1, n):
                    input()
                return sum(l)
    return 0

for idx in range(1, t+1):
    n, m = map(int, input().split())
    res = find_code()
    print('#{} {}'.format(idx, res))