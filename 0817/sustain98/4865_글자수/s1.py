import sys
from collections import Counter
sys.stdin = open('input.txt')

t = int(input())
for idx in range(1,t+1):
    str1 = input()
    str2 = input()

    d = Counter(str2)
    res = 0
    for c in set(str1):
        if c in d.keys() and res < d[c]:
            res = d[c]
    print('#{} {}'.format(idx, res))

