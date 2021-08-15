def BubbleSort(a):
    for i in range(len(a)-1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

def Counting_Sort(a):
    k = a[0]
    for i in range(len(a)):
        if a[i] > k:
            k = a[i]

    c = [0] * (k+1)
    b = [0] * len(a)

    for i in range(0, len(a)):
        c[a[i]] += 1

    for i in range(1, len(c)):
        c[i] += c[i-1]

    for i in range(len(a)-1, -1, -1):
        c[a[i]] -= 1
        b[c[a[i]]] = a[i]

    return b

def selection_sort(nums):
    for i in range(0, len(nums)-1):
        my_min = i
        for j in range(i+1, len(nums)):
            if nums[my_min] > nums[j]:
                my_min = j
        nums[i], nums[my_min] = nums[my_min], nums[i]
    return nums

import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    my_list = list(map(int, input().split()))

    # print('#{} {}'.format(test_case, *selection_sort(my_list))) 왜 이렇게 출력하면 안되는지 몰르겠다!!!
    # print(BubbleSort(my_list))
    # print(Counting_Sort(my_list))
    print('#{}'.format(test_case), end=' ')
    print(*selection_sort(my_list))