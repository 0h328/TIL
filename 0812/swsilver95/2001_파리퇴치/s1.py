import sys

sys.stdin = open('input.txt')

T = int(input())
for idx in range(1, T + 1):
    N, M = map(int, input().split())
    data = []
    for _ in range(N):                              # 이차원배열 형태로 데이터를 저장
        data.append(list(map(int, input().split())))
    # print(data)

    result = []
    for i in range(N - M + 1):                      # 슬라이싱 방법을 통해서 해결
        for j in range(N - M + 1):                  # 인덱스를 초과하지 않는 범위를 찾아서 range값을 지정
            fly = []                                # 파리채 안에 들어가는 숫자 배열
            for k in range(M):                      # 파리채의 크기 M 만큼 반복
                fly += data[i+k][j:j+M]             # 데이터를 슬라이싱해서 원하는 파리채 타격 범위를 뜯어냄
                # print(fly)
                if len(result) == 0:                # 만약 결과 배열의 길이가 0이면
                    result.append(sum(fly))         # 파리의 개수를 더해서 추가
                else:                               # 결과 배열에 무슨 값이 있다면
                    if result[-1] <= sum(fly):      # 결과 배열의 맨 뒤의 값과 현재 파리 수를 비교해서 현재 파리 수가 크다면
                        result.append(sum(fly))     # 결과 배열에 추가


    print('#{} {}'.format(idx, result[-1]))         # 결과 배열의 가장 뒷값이 최대가 되므로, 가장 뒤의 값을 출력