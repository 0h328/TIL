import sys
sys.stdin = open('input.txt')

T = int(input())


for num in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    my_max = arr[0]
    my_min = arr[0]

    for i in range(N):

        if arr[i] > my_max:
            my_max = arr[i]

        if arr[i] < my_min:
            my_min = arr[i]

        result = my_max - my_min

    print("#{} {}".format(num, result))


