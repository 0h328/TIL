import sys
sys.stdin = open('input.txt')

for T in range(int(input())):
    length = int(input())
    arr = list(map(int, input().split()))
    b = 0
    for i in range(length-1):
        for j in range(i, length):
            if b%2:
                # 가장 작은 값
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
            else:
                # 가장 큰 값
                if arr[i] < arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
        b+=1

    print('#{}'.format((T+1)), end=' ')
    print(*arr[:10])

#1 10 1 9 2 8 3 7 4 6 5
#2 89 8 85 11 67 16 60 28 49 39
#3 98 3 97 9 88 17 75 18 71 21