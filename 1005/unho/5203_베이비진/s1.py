import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):
    num_li = list(map(int, input().split()))
    answer = 0
    one, two = [0] * 10, [0] * 10

    for idx in range(12):
        if not idx%2:                   # 카운트 추가
            one[num_li[idx]] += 1
        else:
            two[num_li[idx]] += 1

        for idx in range(10):           # 카운트 리스트 0부터 9까지 순회
            if two[idx] >= 3:           # 플레이어 2 / 현재 숫자 3개 이상인 경우 승
                answer = 2
                break
            elif idx < 8:              # 연속적인숫자 체크
                for j in range(3):
                    if not two[idx+j]:
                        break
                else:
                    answer = 2
                    break

            if one[idx] >= 3:
                answer = 1
                break
            elif idx < 8:
                for j in range(3):
                    if not one[idx+j]:
                        break
                else:
                    answer = 1
                    break
        if answer:
            break
    
    print('#{} {}'.format(tc, answer))