import sys
sys.stdin = open('input.txt')

money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
T = int(input())
for t in range(1, T+1):
    N = int(input())
    pay = [0] * 8
    for i in range(8):
        pay[i] = N // money[i]
        N = N % money[i]
    print('#{}'.format(t))
    print(*pay)