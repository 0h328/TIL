import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    p = input()
    text = input()

    n = len(text)
    m = len(p)

    i = 0
    j = 0
    while i < n and j < m:
        if text[i] != p[j]:
            i -= j
            j = -1
        i += 1
        j += 1
    if j == m:
        print('#{} 1'.format(tc))
    else:
        print('#{} 0'.format(tc))