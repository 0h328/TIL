import sys
sys.stdin = open('input.txt')

original_set = list(map(int, input().split()))
bit = [0] * len(original_set)
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
                        for p in range(len(original_set)):
                            if bit[p]:
                                print(original_set[p], end=' ')
                        print()