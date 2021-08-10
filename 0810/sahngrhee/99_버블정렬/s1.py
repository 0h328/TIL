import sys
sys.stdin = open('input.txt')

def BubbleSort(a):
    for i in range(len(a)-1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

my_list = list(map(int, input().split()))
print(BubbleSort(my_list))
