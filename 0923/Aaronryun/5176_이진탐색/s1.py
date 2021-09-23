import sys
sys.stdin=open('input.txt')

def search(start):
    global temp,result

    if start <= N:
        search(start*2)
        temp+=1
        result[start]=temp
        search(start*2+1)

    return

for test in range(1,1+int(input())):
    N = int(input())

    temp = 0
    result = [0]*(N+1)

    search(1)

    print('#{} {} {}'.format(test,result[1],result[N//2]))