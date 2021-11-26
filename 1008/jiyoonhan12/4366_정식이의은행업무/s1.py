import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    bi = list(input())
    te = list(input())
    bi_compare, te_compare = set(), set()
    for i in range(len(bi)*2):
        bi_copy = bi[:]
        bi_copy[i//2] = str(i%2)
        bi_compare.add(int(''.join(bi_copy), 2))
    for j in range(len(te)*3):
        te_copy = te[:]
        te_copy[j//3] = str(j%3)
        te_compare.add(int(''.join(te_copy), 3))
    print('#{} {}'.format(t, (bi_compare & te_compare).pop()))