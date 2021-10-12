import sys
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    N = int(input())//10
    check = [0, 1]
    for i in range(2, N+1):
        if i % 2:
            check.append(check[i-1]*2-1)
        else:
            check.append(check[i-1]*2+1)

    print(check)