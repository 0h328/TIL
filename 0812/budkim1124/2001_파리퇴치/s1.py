import sys
sys.stdin = open('input.txt')

T = int(input())

for num1 in range(T):
    array = []

    N, M = list(map(int, input().split()))

    for a in range(N):
        arr = list(map(int, input().split()))
        array.append(arr)

    tot_list = []

    for i in range(0, N-M+1):
        for j in range(0, N-M+1):
            tot = 0
            for m in range(M):
                for n in range(M):
                    tot += array[i+m][j+n]
            tot_list.append(tot)
    print("#{} {}".format(num1+1, max(tot_list)))