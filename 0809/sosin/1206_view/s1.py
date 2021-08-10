import sys
sys.stdin = open('input.txt')

for T in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))
    # 조망권이 확보된 수
    result = 0
    for i in range(2, len(buildings)-2):
        # 현재 높이 저장
        temp = buildings[i]
        # 앞뒤로 2칸 비교
        for j in range(-2, 3):
            # 하나라도 클 시 break
            if buildings[i] < buildings[i+j]:
                break
            # 같은 건물이면 넘기기
            elif i == i+j:
                continue
            # 낮은 층이면 그 층수만큼 빼고 저장
            # 더 높은 건물이 있으면 그만큼 조망권이 줄어듦으로 min으로 체크
            else:
                temp = min(temp, buildings[i] - buildings[i+j])
        # for문 끝나면 현재건물의 조망권이 확보된 수를 더함
        else:
            result += temp
        
    print('#{} {}'.format(T, result))
