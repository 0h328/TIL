import sys
sys.stdin = open('input.txt')

for _ in range(10) :
    tc = int(input())

    arr = []
    for i in range(100) :
        arr.append(list(map(int, input().split())))

    sum(arr[0])
    print()