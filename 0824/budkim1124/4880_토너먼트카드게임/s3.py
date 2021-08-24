def battle(i, j):
    if i == j:
        return i

    x = battle(i, (i+j)//2)
    y = battle((i+j)//2+1, j)

    if arr[x] == 1:
        if arr[y] == 2:
            return y
        elif arr[y] == 3:
            return x
        elif arr[y] == 1:
            return x
    if arr[x] == 2:
        if arr[y] == 1:
            return x
        elif arr[y] == 3:
            return y
        elif arr[y] == 2:
            return x
    if arr[x] == 3:
        if arr[y] == 1:
            return y
        elif arr[y] == 2:
            return x
        elif arr[y] == 3:
            return x

import sys
sys.stdin = open("input.txt")

T = int(input())
for num in range(T):
    N = int(input())
    arr = [0] + list(map(int,input().split()))

    print("#{} {}".format(num+1, battle(1,N)))

