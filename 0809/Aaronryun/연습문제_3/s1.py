import sys
sys.stdin = open('input.txt')

T = int(input())
for test in range(T):
    N = int(input())

    numbers = list(map(int,input().split()))

    result = []

    for i in range(len(numbers)):
        cnt = 0
        for j in range(i,len(numbers)):
            if numbers[i] > numbers[j]:
                cnt += 1
        result.append(cnt)

    print(max(result))

