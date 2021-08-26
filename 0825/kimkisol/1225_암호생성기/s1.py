import sys

sys.stdin = open('input.txt')


def Password():
    global Q
    while True:
        for i in range(1, 6):
            new_num = Q.pop(0) - i
            if new_num <= 0:
                Q.append(0)
                return
            Q.append(new_num)


for _ in range(1, 11):
    t = input()
    Q = list(map(int, input().split()))
    Password()

    print('#{}'.format(t), end=' ')
    print(*Q) #format print 사용 불가
