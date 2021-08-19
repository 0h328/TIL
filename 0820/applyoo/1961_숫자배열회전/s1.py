import sys
sys.stdin = open('input.txt')

import copy


def arr_column(arr, column):  # 2중 리스트에서 컬럼을 반환하는 함수
    result = []  # column번째 열의 값들을 저장할 공간

    for i in range(len(arr)):
        result.append(arr[i][column])

    return result


def rotation(arr, degree):  # 90배수 각도의 회전한 2중 리스트를 반환하는 함수
    degree = degree % 361  # 360도가 넘는 경우 불필요한 재귀의 반복을 제한하기 위해 변주 재지정

    if degree == 90:  # 90도 일때
        new_arr = copy.deepcopy(arr)  # 90도 회전된 값을 저장할 공간(2중 리스트 복사는 deepcopy를 활용해야 함)
        for i in range(len(arr)):
            new_arr[i] = arr_column(arr, i)[::-1]  # arr_column 함수에서 반환된 값의 역수를 저장해야 함
        return new_arr
    else:  # 90도가 아닌 90의 배수일 때
        new_arr = rotation(arr, degree - 90)  # degree - 90의 표현을 통해 Base case가 위의 90도 일때에 걸리게 만듬
        return rotation(new_arr, 90)  # 최종 반환된 new_arry에서 한번 더 90도 돌린 값을 반환해야 degree의 각도를 회전한 값이 됨


T = int(input())

for test in range(T):
    N = int(input())
    N_list = [[0] * N for _ in range(N)]  # 값을 입력받을 2중 리스트 생성(for문 이용!)
    for i in range(N):
        N_list[i] = list(map(int, input().split()))

    N_list_90 = rotation(N_list, 90)  # 90도 돌린 2중 리스트
    N_list_180 = rotation(N_list, 180)
    N_list_270 = rotation(N_list, 270)

    print('#{}'.format(test+1))
    for j in range(N):
        print(*N_list_90[j], sep='', end=' ')  # unpack으로 리스트 내의 리스트를 출력하고, sep을 통해 구분자 지정가능
        print(*N_list_180[j], sep='', end=' ')
        print(*N_list_270[j], sep='')