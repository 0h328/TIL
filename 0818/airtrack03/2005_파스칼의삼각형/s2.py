# stack 풀이

import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    triangle_line = [1]     # 처음 시작은 1
    cnt = 0

    print('#{}'.format(tc))

    while cnt < N:
        print(' '.join(map(str, triangle_line)))
        new_line = []       # 다음 줄을 저장할 리스트
        temp = 0            # 처음 숫자는 0 + 1이므로 temp는 0으로 설정. 현재 pop 이전에 pop한 숫자 저장
        while triangle_line:
            num = triangle_line.pop()   # 현재 pop하는 숫자 저장
            new_line.append(temp + num) # 현재 pop한 숫자와 이전에 pop한 숫자 더해서 append
            temp = num      # temp를 현재 pop한 숫자로 바꿔줌
        new_line.append(1)  # 끝에 1을 append
        triangle_line = new_line[:] # new_line이 이제 pop한 line이 된다
        cnt += 1