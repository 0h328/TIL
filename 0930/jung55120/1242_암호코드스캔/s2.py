import sys
sys.stdin = open('input.txt')

amho = {  # 딕셔너리
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lines = set()
    for _ in range(N):
        temp = input().strip('0')
        if len(temp) == 0: continue
        temp = bin(int(temp, 16))[2:].rstrip('0')
        lines.add(temp)

    for line in lines:
        line = line.zfill(56)
        print(line)
