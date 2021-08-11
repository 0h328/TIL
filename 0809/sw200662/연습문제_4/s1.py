import sys
sys.stdin = open('input.txt')

N = int(input())


for i in range(N):
    num = int(input())
    count = [0] * 12
    check = 0
    triplet = run = 0
    for k in range(6):
        count[num % 10] += 1
        num //= 10

    while check < 10:
        if count[check] >= 3:
            count[check] -= 3
            triplet += 1
            continue;

        if count[check] >= 1 and count[check+1] >= 1 and count[check+2] >= 1:
            count[check] -= 1
            count[check+1] -= 1
            count[check+2] -= 1
            run += 1
            continue;

        check += 1
    if triplet + run == 2:
        print('#{} 1'.format(i+1))
    else:
        print('#{} 0'.format(i+1))



