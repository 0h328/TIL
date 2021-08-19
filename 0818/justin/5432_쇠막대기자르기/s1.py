import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    iron_bar = input()
    cnt = 0             # 막대수
    ans = 0             # 쇠막대기 조각의 총 개수

    for i in range(len(iron_bar)):  # 괄호의 수만큼 반복을 돌며
        if iron_bar[i] == '(':      # 여는 괄호는 막대 추가
            cnt += 1                # 막대 추가
        else:                       # 닫힌 괄호는
            cnt -= 1                # 일단 빼자 (레이저라면 당연히 잘못 카운트 했으니 빼고 아니라면 어차피 막대 끝이니 빼자)
            if iron_bar[i-1] == '(':  # 이전이 여는 괄호였다면 레이저
                ans += cnt            # 레이저로 인해서 잘린 막대들이 생겼으므로 개수 누적
            else:                     # 이전이 닫는 괄호였다면
                ans += 1              # 막대 끝이기 때문에 조각 1개만 추가
    print('#{} {}'.format(tc, ans))