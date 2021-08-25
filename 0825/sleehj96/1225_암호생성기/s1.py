import sys
sys.stdin = open('input.txt')

T = 10
tc = 1
while tc <= T:
    input()
    q = list(map(int,input().split()))

    n = 0
    while True:
        n += 1
        v = q.pop(0)
        new_num = v - n

        if new_num <= 0:
            new_num = 0
            q.append(new_num)
            break

        q.append(new_num)
        n %= 5

    print('#{}'.format(tc), *q)
    tc += 1
