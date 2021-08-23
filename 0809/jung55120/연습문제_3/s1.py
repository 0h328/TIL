import sys
sys.stdin = open('input.txt')

def gravity() :
    result = 0

    for i in range(length) :
        for j in range(1, arr[i]+1) :
            cnt = 0
            for k in range(i, length) :
                if arr[k] >= j :
                    cnt += 1
            result = max(result, length - cnt - i)

    return result

T = int(input())

for a in range(T) :
    length = int(input())
    arr = list(map(int,input().split()))

    print('#{0} {1}'.format(a+1, gravity()))

















