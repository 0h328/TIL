import sys
sys.stdin = open('input.txt')

for num in range(10):
    N, s = input().split()
    arr = []
    arr.extend(s)
    print(arr)
    tmp = ['1']

    while tmp:
        tmp = []
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:
                del arr[i-1:i+1]
                tmp.append(i)



