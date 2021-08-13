import sys
from collections import deque

sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    data.sort()     # 입력 리스트 오름차순 정렬
    data = deque(data)  # 양쪽에서 데이터 pop 위해 deque로 변환
    ans = []    # 특별하게 정렬된 숫자 담을 리스트
    cnt = 0     # 홀수, 짝수 구분 위한 변수

    while data:
        if cnt % 2:
            ans.append(data.popleft())  # 현재 리스트의 가장 작은 수
        else:
            ans.append(data.pop())  # 현재 리스트의 가장 큰 수
        cnt += 1
    ans = ans[:10]  # 10개까지만 출력해야 하므로
    print('#{} {}'.format(tc, ' '.join(list(map(str, ans)))))