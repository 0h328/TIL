import sys

sys.stdin = open('input.txt', encoding='UTF8')

def search(target,pattern):
    N = len(target)
    M = len(pattern)
    i=0
    j=0
    cnt = 0
    while i<N and j<M:
        if target[i] != pattern[j]:
            i = i-j
            j=-1
        i+=1
        j+=1
        if j == M:
            cnt+=1
            j=0
    return cnt

for test in range(10):

    number = input()
    pattern = input()
    target = input()

    print('#{} {}'.format(test+1,search(target,pattern)))