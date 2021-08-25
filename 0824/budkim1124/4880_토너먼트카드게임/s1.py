import sys
sys.stdin = open("input.txt")

T = int(input())
for num in  range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    stack = arr[:]
    arr_idx = []
    while len(arr) != 1:
        arr_idx.append(arr)
        arr = stack[:]
        for i in range(1, len(arr), 2):
            if (arr[i] == 1 and arr[i-1] == 3) or (arr[i] == 2 and arr[i-1] == 3) or (arr[i] == 3 and arr[i-1] == 1):
                stack.remove(arr[i-1])
            else:
                stack.remove(arr[i - 1])

    for result in arr:
        print("#{} {}".format(num+1, result))
