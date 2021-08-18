import sys
sys.stdin = open('input.txt')

t = int(input())                    # 테스트 케이스 갯수
for tc in range(t):                 # 테스트 케이스 갯수만큼 반복
    case = int(input())             # 몇 번째 줄 까지 파스칼 삼각형 표현할지 정함
    print("#{0}".format(tc + 1))    # 테스트 케이스 번호 출력

    result = []                     # 결과 담을 배열
    for r in range(1, case + 1):    # case 줄까지 반복
        temp = []                   # 각 줄 마다 배열
        for c in range(1, r + 1):   # 각 줄 마다 갯수만큼 반복
            if (r <= 2) or (c == 1) or (c == r):    # 2줄 이하이거나 각 줄마다 첫번째나 마지막 열이면
                temp.append(1)      # 1을 삽입
            else:                   # 그 외 중간 부분에는
                temp.append(result[r - 2][c - 2] + result[r - 2][c - 1])
                # 이전 단계 좌 우의 합 (ex) 1 = 0 + 1, 2 = 1 + 2, 3 = 2 + 3)
        result.append(temp)         # result에 각 줄을 리스트로 담음

    for res in result:              # result 갯수만큼 담음
        for re in res:              # 각 줄마다 갯수만큼 반복
            print(re, end=" ")      # 띄어쓰면서 하나씩 출력
        print()                     # 줄바꿈
