import sys
sys.stdin = open('input.txt')

t = int(input())
for num in range(1, t+1):
    l = [input() for _ in range(5)]
    length = max(map(len, l))
    res = [''] * length
    for s in l:
        for i in range(len(s)):
            res[i] += s[i]
    print('#{} {}'.format(num, ''.join(res)))

