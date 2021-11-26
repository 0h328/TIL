import sys
sys.stdin = open('input.txt')

T = int(input())

for num in range(T):
    words1 = input()
    words2 = input()
    cnt = 0

    if words1 in words2:
        cnt += 1

    print("#{} {}".format(num+1, cnt))