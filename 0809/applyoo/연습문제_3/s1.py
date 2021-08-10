import sys
sys.stdin = open('input.txt')

def gravity():
    result = 0

    for i in range(length): # 칸을 반복(열)
        for j in range(1, arr[i]+1): # 해당 칸의 높이를 반복
            cnt = 0 # 오른쪽에 블럭이 몇 개 있는지 카운트할 변수
            for k in range(i, length): # 해당 칸 ~ 끝까지만 계산
                if arr[k] >= j: # 비교할 칸이 j(높이)보다 크거나 같은 경우
                    cnt += 1 # 카운팅
            result = max(result, length - cnt - i) # (기존 값)과 (길이-카운팅-해당 칸 번호) 중 큰 값 선택

    return result # 결과 반환

T = int(input())

for _ in range(T):
    length = int(input())
    arr = list(map(int, input().split()))

    print(gravity())