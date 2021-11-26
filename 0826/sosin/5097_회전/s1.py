import sys
sys.stdin = open('input.txt')

for T in range(int(input())):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    print('#{} {}'.format((T+1), arr[M%N]))

#1 731
#2 18641
#3 2412