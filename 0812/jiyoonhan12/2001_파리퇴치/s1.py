import sys
sys.stdin = open('input.txt')

T =  int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)] # 파리배치도

    max_group = 0 # 최대로 죽일 수 있는 파리 변수
    for i in range(N-M+1): # n*n 배열에서 m*m 들어갈 수 있는 만큼
        for j in range(N-M+1):
            current_group = 0 # m*m 더해줄 임시변수
            for k in range(M):
                for l in range(M):
                    current_group += arr[i+k][j+l] # 더해...
            if current_group > max_group: # 최대값 바꿔줘...
                max_group = current_group

    print('#{} {}'.format(t, max_group))