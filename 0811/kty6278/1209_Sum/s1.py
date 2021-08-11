# input 데이터를 불러온다.
import sys
sys.stdin = open('input.txt')

for test in range(10):
    box_list = []
    nums = int(input())
    for _ in range(100):
        box = list(map(int, input().split()))
        box_list.append(box)

    total_list = []
    for i in range(100):
        total = 0
        for j in range(100):
            total += box_list[i][j]
        total_list.append(total)

    for j in range(100):
        total = 0
        for i in range(100):
            total += box_list[i][j]
        total_list.append(total)

    fir_list = []
    sec_list = []
    for i in range(100):
        first = 0
        for j in range(100):
            if i == j:
                first += box_list[i][j]
        fir_list.append(first)
    total_list.append(sum(fir_list))

    for i in range(100):
        second = 0
        for j in range(100):
            if 99 - i == j:
                second += box_list[i][j]
        sec_list.append(second)
    total_list.append(sum(sec_list))
    print('#{} {}'.format(test+1, max(total_list)))