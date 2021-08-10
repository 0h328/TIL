import sys                                  # open을 쓰기 위한 모듈
sys.stdin = open('input.txt')               # input.txt 파일을 불러옴

for number in range(0, 10):                 # 총 10개의 테스트 케이스 갯수
    N = int(input())                        # 가로 길이
    M = list(map(int, input().split()))     # 각 빌딩의 높이를 담은 리스트
    building_min = M[2]                     # building_min에 처음 빌딩 높이를 담음
    result = 0                              # result에 0을 담음
    for i in range(2, N-2):                 # 2부터 N-3까지 반복을 돌림 (빌딩은 3칸 째부터 N-3칸 째까지 있기 때문)
       building_min = min(M[i] - M[i - 2], M[i] - M[i - 1], M[i] - M[i + 1], M[i] - M[i + 2])   # M[i]를 기준으로 -2 ~ +2칸 까지 비교해서 가장 작은 값을 building_min에 담음
       if (building_min > 0):               # building_min이 양수이면
           result += building_min           # 그 수만큼 조망권이 확보된 층이므로 result에 더해나감
    print("#{0} {1}".format(number + 1, result))    # #number + 1 과 조망권의 합 result를 출력