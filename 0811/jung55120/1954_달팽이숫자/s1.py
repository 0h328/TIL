import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    num = int(input())
    arr = []
    for i in range(num) :
        for j in range(num) :
            arr.append(arr[i][j])
