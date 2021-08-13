import sys
sys.stdin = open('input.txt')


def selection_sort(a):
    for i in range(len(a)-1):
        min = i
        for j in range(i+1,len(a)):
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min], a[i]
    return(numbers)



numbers = list(map(int, input().split()))
print(selection_sort(numbers))