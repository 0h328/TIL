import sys
sys.stdin = open('input.txt')

arr = [i for i in range(1, 13)]

for T in range(int(input())):
    N, S = map(int, input().split())
    result = 0
    for i in range(1<<(N-1), 1<<12):
        temp = 0
        count = 0
        for j in range(12):
            if count > N:
                break
            
            if i & (1<<j):
                count += 1
                temp += arr[j]

        if count == N and S == temp:
            result+=1

    print('#{} {}'.format((T+1), result))

#1 1
#2 1
#3 0