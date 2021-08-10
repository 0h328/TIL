import sys
sys.stdin = open('input.txt')

num_list = list(map(int, input().split()))


def bubble_sort(lst):

    for idx in range(len(lst) - 1, 0, -1):
        for idx2 in range(idx):
            if lst[idx2] > lst[idx2+1]:
                lst[idx2], lst[idx2+1] = lst[idx2+1], lst[idx2]

    return lst


print(bubble_sort(num_list))
