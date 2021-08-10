import sys
sys.stdin = open('input.txt')

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

my_list = list(map(int, input().split()))
print(Counting_Sort(my_list))












