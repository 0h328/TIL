import sys
sys.stdin = open('input.txt')

T = int(input())

for i in range(T):
    N,M = map(int,input().split())

    Num_list = list(map(int,input().split()))

    for _ in range(M):
        Num_list.append(Num_list.pop(0))
    print('#{} {}'.format(i+1,Num_list[0]))
