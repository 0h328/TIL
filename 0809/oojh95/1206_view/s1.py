# 코드가 들어가는 파일
import sys
sys.stdin = open('input.txt')

T = 10
for test_case in range(1, T+1): # 테스트케이스 동안 진행
    length = int(input())   #처음받는 가로 길이
    build_list = list(map(int, input().split()))    # 빌딩의 높이리스트

    cnt = 0
    for i in range(2, length-2):    # 시작과 끝을 2칸씩 띄우고 건물 높이 비교
        max_height = 0  # 기준 건물 좌우로 최고 높이를 0으로 초기화
        for j in range(-2, 3):  # -2부터 2까지 하는데 0일때는 건물 본인의 높이이므로 continue
            if j == 0:
                continue
            elif build_list[i+j] > max_height:  # 주변 최대높이중 가장 높은지 확인 맞으면 갱신
                max_height = build_list[i+j]
        if build_list[i] - max_height > 0:  # 최대 높이보다 본 건물의 높이가 큰 경우 그 차이만큼이 조망권이 확보된다.
            cnt += build_list[i] - max_height

    print('#{} {}'.format(test_case, cnt))