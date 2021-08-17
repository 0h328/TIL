import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(t):
    A, B = input().split()

    temp = A.count(B)
    result = len(A) - temp * len(B) + temp
    print("#{0} {1}".format(tc + 1, result))