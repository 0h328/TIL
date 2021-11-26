# input 데이터를 불러온다.
import sys
sys.stdin = open('input.txt')

arr = list(map(int, input().split()))
bit = [0] * 6
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                for m in range(2):
                    bit[4] = m
                    for n in range(2):
                        bit[5] = n
                        # print(bit)
                        for p in range(6):
                            if bit[p]:
                                print(arr[p], end = ' ')
                        print()