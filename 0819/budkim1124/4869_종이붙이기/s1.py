import sys
sys.stdin = open('input.txt')
T = int(input())

for num in range(T):
    N = int(input())
    arr = [0 for j in range(N//10+1)]
    arr[0] = 1
    arr[1] = 1

    for i in range(2, N // 10 +1):
        arr[i] = arr[i-1] + (arr[i-2]*2)

        if i == N // 10:
            print("#{} {}".format(num+1, arr[i]))