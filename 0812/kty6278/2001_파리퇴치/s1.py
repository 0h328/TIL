import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())

    new_list = []
    for n in range(N):
        new_list.append(list(map(int, input().split())))

#   print(new_list)

    max_value = 0 # 죽은 파리 수의 최대 값
    # 파리채의 넓이를 고려한 마지막 지점 n-m+1
    for i in range(N-M+1):
        for ii in range(N-M+1):

            total = 0 # 죽은 파리 수
            for j in range(M): # 파리채의 크기만큼
                for jj in range(M):
                    total += new_list[i+j][ii+jj]
            if total > max_value:
                max_value = total

    print(f'#{t} {max_value}')