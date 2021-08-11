import sys
sys.stdin = open('input.txt')

T = int(input())

for idx in range(1, T+1):
    n = int(input())
    blocks = list(map(int, input().split()))
    # (직관) 상자는 항상 제일 끝에서 낙차가 최대가 될 것이다.

    drop = []                               # 각 칸별 최대 낙차를 기록
    for i in range(len(blocks) - 1):        # 인덱스 순회 방식으로 해결
        tmp = blocks[i]
        cnt = 0
        for j in range(i, len(blocks)):
            if tmp > blocks[j]:             # 기준 블록 값 우측으로 더 높이가 작은 블록이 있다면
                cnt += 1                    # count에 1을 더해줌
        drop.append(cnt)                    # 최종적으로 각 칸별 낙차를 drop 리스트에 추가

    print('#{0} {1}'.format(idx, max(drop)))

