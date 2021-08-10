import sys
sys.stdin = open('input.txt')

num = list(map(int, input().split()))

def bubble_sort(num):

    for i in range(len(num)-1, 1, -1):
        for j in range(0, i):
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]
    return num

print(bubble_sort(num))