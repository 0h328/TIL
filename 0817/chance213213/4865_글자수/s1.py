import sys
sys.stdin = open('input.txt')

N = int(input())

for tc in range(N):
    # A = []
    # A.extend(input())
    A = input() #원래는 들어올 때부터, string 한글자씩 들어옴
    # B = []
    # B.extend(input())
    B = input()
    Ac = [0]*len(A)


    for idx in range(len(A)):
        cnt = B.count(A[idx])
        Ac[idx] += cnt

    # print(Ac)

    print('#{} {}'.format(tc+1, max(Ac)))

