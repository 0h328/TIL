import sys
sys.stdin = open('input.txt')

T = int(input())

for num in range(T):
    A, B = map(str, input().split())
    cnt = 0

    print("#{} {}".format(num+1, len(A) - (len(B) * A.count(B)) + A.count(B)))
