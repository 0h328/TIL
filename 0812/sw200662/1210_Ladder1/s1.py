import sys

sys.stdin = open('input.txt')

for i in range(10):
    T = int(input())
    list1 = []
    list2 = []
    x = y = 0

    for _ in range(100):
        list2 = list(map(int, input().split()))
        list1.append(list2)

    for k in range(100):
        if list1[99][k] == 2:
            x = k
        y = 99

    while True:
        if x > 0 and list1[y][x - 1]:
            while x > 0 and list1[y][x - 1]:
                x -= 1
            else:
                y -= 1

        elif x < 99 and list1[y][x + 1]:
            while x < 99 and list1[y][x + 1]:
                x += 1
            else:
                y -= 1

        else:
            y -=1

        if y == 0:
            break
    print('#{} {}'.format(i + 1, x))
