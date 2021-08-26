import sys
sys.stdin = open('input.txt')

for i in range(10):
    N = int(input())
    Nums = list(map(int,input().split()))
    start = 0
    while True:
        for k in range(1,6):
            A = Nums[start] - k
            start += 1
            if A <= 0:
                A = 0
            Nums.append(A)
            if A == 0:
                break

        if A == 0:
            break
    print('#{}'.format(i+1),end= ' ')
    for z in Nums[start:]:
        print(z,end=' ')
    print()
