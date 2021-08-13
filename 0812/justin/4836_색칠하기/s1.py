import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    boxes = [[0] * 10 for _ in range(10)]
    n = int(input())
    cnt = 0
    for k in range(n):       # 박스에 색상 칠하기
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                boxes[i][j] += color

    for i in range(10):      # 겹쳐진 칸수 카운팅 -> 3이면 겹쳐진 영역
        for j in range(10):
            if boxes[i][j] == 3:
                cnt += 1

    # 이 문제를 조금 더 어렵게 만들면 어떤 조건을 넣어줄 수 있을까요?
    # 고민해봅시다!
    print('#{} {}'.format(tc, cnt))