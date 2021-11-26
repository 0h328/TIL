import sys
sys.stdin = open('input.txt')

T = int(input())

for num in range(T):
    string = input()
    arr = []
    arr.extend(string)
    cnt = 1
    while cnt != 0:
        cnt = 0
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:
                cnt += 1
                del arr[i-1:i+1]
                break

    print("#{} {}".format(num+1, len(arr)))
