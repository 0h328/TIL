import sys
sys.stdin = open('input.txt')

def bubblesort(a):
    for i in range(len(a)-1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

num = int(input())
for _ in range(num):
    cnt_list = list(map(int,input().split()))
    print(bubblesort(cnt_list))