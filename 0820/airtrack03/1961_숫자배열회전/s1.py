import sys

sys.stdin = open('input.txt')

T = int(input())

def rotate_90(lst):     # 배열 90도 회전 함수
    N = len(lst)
    rotated = [[0] * N for _ in range(N)]

    for row in range(N):
        for col in range(N):
            rotated[row][col] = lst[N-col-1][row]

    return rotated

for tc in range(1, T+1):
    N = int(input())
    data = []
    for _ in range(N):
        data.append(input().split())

    r_90 = rotate_90(data)      # 원본 데이터 90도 회전 리스트
    r_180 = rotate_90(r_90)     # 90도 회전 리스트를 다시 90도 회전
    r_270 = rotate_90(r_180)    # 180도 회전 리스트를 90도 회전

    # 정답 출력 위해 문자열로 전환
    r_90_str = [''.join(lst_row) for lst_row in r_90]
    r_180_str = [''.join(lst_row) for lst_row in r_180]
    r_270_str = [''.join(lst_row) for lst_row in r_270]

    print('#{}'.format(tc))
    # 한 줄로 출력 위해 zip함수 활용
    for num_str in zip(r_90_str, r_180_str, r_270_str):
        print(' '.join(num_str))