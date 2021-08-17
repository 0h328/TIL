import sys
sys.stdin = open('input.txt')

T = int(input())

for num in range(T):
    A, B = map(str, input().split())
    cnt = 0

    result = len(A) - (len(B) * A.count(B)) + A.count(B)

    print("#{} {}".format(num+1, result))
