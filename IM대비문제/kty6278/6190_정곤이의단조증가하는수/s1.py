import sys
sys.stdin = open('input.txt')

def is_dan(num):
    num = str(num)
    for k in range(len(num)-1):
        if num[k] > num[k + 1]:
            return False
    return True


for tc in range(int(input())):
    N = int(input())
    num = list(map(int, input().split()))
    res = -1
    for i in range(N):
        for j in range(i+1, N):
            math = num[i] * num[j]
            if res < math and is_dan(math):
                res = math
    print('#{} {}'.format(tc+1, res))