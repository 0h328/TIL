import sys
sys.stdin = open('input.txt')

L = list(map(int, input().split()))

N = len(L)

for i in range(1, 1<<N):       # 2의 N승 (1을 왼쪽으로 N칸, 2진법)
    for j in range(N):
        if i & (1<<j):      # j의 N승 / 찾고자 하는 자리에 1이 있는가?
            print(L[j], end= ' ')
    print()


num = [1, 2, 3, 4]
bits = [0, 0, 0, 0]

for i in range(2):
    bits[0] = i
    for j in range(2):
        bits[1] = j
        for k in range(2):
            bits[2] = k
            for l in range(2):
                bits[3] = l
                for z in range(4):
                    if bits[z] == 1:
                        print(num[z], end= ' ')
                print()