import sys
sys.stdin = open('input.txt', encoding='UTF-8')

for _ in range(10):
    n = int(input())
    p = input()
    t = input()

    cnt = 0
    for i in range(len(t)-1):
        if t[i:len(p)+i] == p:
            cnt += 1

    print('#{} {}'.format(n, cnt))