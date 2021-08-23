import sys
sys.stdin = open('input.txt')

T = int(input())

for num in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    result = []

    for i in range(10):
        if i % 2 == 0:
            result.append(max(arr))
            arr.remove(max(arr))
        else:
            result.append(min(arr))
            arr.remove(min(arr))

    
    print('#{}'.format(num+1), end=' ')
    for i in range(10):
        print(result[i], end=" ")
    print()