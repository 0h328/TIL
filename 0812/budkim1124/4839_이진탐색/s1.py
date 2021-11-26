import sys
sys.stdin = open('input.txt')

def binary_search(r, target):

    x = 1
    cnt = 0
    while x <= r:
        c = int((x + r) / 2)
        if c < target:
            x = c+1
            cnt += 1
        elif c == target:
            return cnt
        else:
            r = c - 1
            cnt += 1
    return cnt


T = int(input())
result = 0
for num in range(T):
    R, A, B = list(map(int, input().split()))

    if binary_search(R, A) < binary_search(R, B):
        result = 'A'
    elif binary_search(R, A) > binary_search(R, B):
        result = 'B'
    elif binary_search(R, A) == binary_search(R, B):
        result = '0'


    print("#{} {}".format(num+1, result))