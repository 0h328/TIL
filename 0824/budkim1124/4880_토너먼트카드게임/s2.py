def battle(i, j):
    if i == j:
        return i

    a_idx = battle(i, (i+j)//2)
    b_idx = battle((i+j)//2+1, j)

    if (arr[a_idx] == 1 and arr[b_idx] == 3) or (arr[a_idx] == 2 and arr[b_idx] == 3) or (arr[a_idx] == 3 and arr[b_idx] == 1):
        return a_idx
    else:
        return b_idx

import sys
sys.stdin = open("input.txt")

T = int(input())
for num in range(T):
    N = int(input())
    arr = [0] + list(map(int,input().split()))

    print("#{} {}".format(num+1, battle(1,N)))

