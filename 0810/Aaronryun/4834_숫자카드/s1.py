import sys

sys.stdin = open('input.txt')

T = int(input())


def BubbleSort(a):
    for i in range(len(a) - 1, 0, -1):
        for j in range(i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


for test in range(T):
    N = int(input())
    data = []
    number = int(input())

    while number > 0:  # 리스트의 형태로 인풋저장
        data.append(number % 10)
        number //= 10

    check = [0] * 12

    for i in data:
        check[i] += 1               # 장수계산을 위해서 리스트에 저장

    real = check[:]                 # 리스트를 복사하고
    BubbleSort(check)               # 원래 리스트는 정렬해서 가장 큰 수 즉 제일 많았던 장수를 찾는다.

    max_num = 0
    num = 0

    for i in range(len(real)):      # 제일 많은 장수가 원래 리스트에서 어떤 위치에 있었는지 확인을 통해 둘다 뽑는다.
        if real[i] == check[-1]:
            max_num = check[-1]
            num = i

    print('#{} {} {}'.format(test + 1, num, max_num))
