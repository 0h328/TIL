# input 데이터를 불러온다.
import sys
sys.stdin = open('input.txt')

# 10개의 테스트 케이스를 실행
for i in range(10):
    # 테스트 케이스 마다 빌딩의 수 데이터를 받아온다.
    nums = int(input())
    # 빌딩 수의 빌딩 높이를 받아온다. 앞의 2개 뒤에 2개 높이가 '0'인 데이터를 포함해서 받아온다.
    height = list(map(int, input().split()))
    # 조망권이 보장이 되는 세대를 구하기 위한 초기 변수 설정
    cnt = 0
    # 빌딩의 수 'nums'로 지정한 변수를 앞, 뒤 2개씩 제외하고 읽어준다.
    for j in range(2, nums-2):
        # 한 개의 빌딩 높이를 기준으로 앞, 뒤 2개씩 총 4개의 빌딩 중 가장 높은 빌딩을 구한다.
        max_height = max(height[j-2], height[j-1], height[j+1], height[j+2])
        # 가장 높은 빌딩의 높이가 위에서 정한 기준 빌딩 높와 비교한다.
        if height[j] > max_height:
            # 기준 빌딩 높이와 4개의 빌딩과의 차이가 존재하는 경우 조망권이 보장되는 세대를 구할 수 있다.
            cnt += height[j] - max_height
    # i+1을 통해 조망권 보장되는 세대 수를 출력해준다.
    print('#{} {}'.format(i+1, cnt))
    이어폰찾아보겠습니다^^