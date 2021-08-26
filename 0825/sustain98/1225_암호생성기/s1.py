import sys
sys.stdin = open('input.txt')

for _ in range(10):
    idx = input()
    l = list(map(int, input().split()))
    i = 0
    while l[i] != 0:
        for j in range(1, 6):
            x = l[i] - j
            if x <= 0:
                l[i] = 0
                break
            else:
                l[i] = x
                i = (i+1) % 8

    print('#{} '.format(idx), end=' ')
    for i in range(i-7, i+1):
        print(l[i], end=' ')
    print()

