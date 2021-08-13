import sys
sys.stdin = open('input.txt')


T = int(input())
for t in range(T):
    num = int(input())
    box = [[0] * 10 for _ in range(10)]  # 테스트 케이스마다 새로운 리스트 생성

    count = 0  # 한개의 테스트 케이스가 끝난 이후에 겹친 부위 초기화
    for _ in range(num):
        x, y, xx, yy, color = map(int, input().split())

        for i in range(x, xx+1): # 칠하는 영역 (2,2)->(4,4)
            for j in range(y, yy+1):
                box[i][j] += color
                if box[i][j] == 3: # 같은 색은 겹치지 않는다.
                    count += 1
    print(count)