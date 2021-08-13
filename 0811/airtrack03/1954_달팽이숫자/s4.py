# 동완님 풀이
import sys
sys.stdin = open('input.txt')

def snail_number(num):
    arr = list(range(1, num + 1)) + list(range(1, num)) # 배열 만들기(각 방향에 규칙으로)
    arr.sort(reverse=True) # 역순 정렬
		# arr의 인덱스%4 => 방향(0,1,2,3) // arr의 인덱스값 => 해당 방향의 숫자의 개수
    result = [[0] * num for _ in range(num)] # 결과를 저장할 2차원 리스트

    row, col, cnt = [0, -1, 0] # 행, 열, 입력값 초기화(열은 처음에 더해지므로 -1로 지정)

    for i in range(len(arr)): # arr의 길이 반복(방향의 갯수를 의미)
        for j in range(arr[i]): # arr의 요소만큼 반복(방향으로 몇 칸 나아가는지 의미)
            if i % 4 == 0: # 오른쪽인 경우
                col += 1 # 첫번째 방향이므로 제일 처음 걸리는 조건(따라서 col 초기값 -1)
            elif i % 4 == 1: # 아래인 경우
                row += 1 # 두번째 방향(따라서 row 초기값 0)
            elif i % 4 == 2: # 왼쪽인 경우
                col -= 1
            else: # 위쪽인 경우
                row -= 1
            cnt += 1 # 하나씩 증가해야함(따라서 cnt 초기값 0으로 함)
            result[row][col] = cnt # 해당 좌표(row, col)에 값(cnt) 입력
    return result

T = int(input())

for test in range(T):
    N = int(input())
    result = snail_number(N)

    print('#{}'.format(test+1))
    for numbers in result:
        print(*numbers)