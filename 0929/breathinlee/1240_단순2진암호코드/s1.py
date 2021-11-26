import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    # 각 row의 우측에서부터 처음 나타나는 1의 위치를 찾음
    for row in range(N):
        arr_row = arr[row]
        if '1' in arr_row:
            opposite_col = arr_row[::-1].index('1')
            break
        else:
            continue

    col = M - opposite_col     # 1의 원래 index를 찾아줌
    num_value = []             # 암호코드를 받기 위한 배열 생성
    patterns = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
    for i in range(8):
        pattern_string = arr[row][col-7*(i+1):col-7*i]  # 뒤에서부터 길이 7칸씩 잘라서 암호코드에 해당하는 숫자 찾기
        if pattern_string in patterns:
            num_value.append(patterns.index(pattern_string))  # 숫자 찾아서 암호코드에 추가
    origin_num_value = num_value[::-1] # 원래의 순서로 나타내기 위해 뒤집음

    even, odd = 0, 0
    for k in range(4):
        # 홀수 index : 0, 2, 4, 6 / 짝수 index : 1, 3, 5 / 검증코드 index : 7
        odd += origin_num_value[2*k]
        even += origin_num_value[2*k + 1]
    code = odd * 3 + even
    if code % 10:
        ans = 0
    else:
        ans = sum(origin_num_value)

    print('#{} {}'.format(tc, ans))