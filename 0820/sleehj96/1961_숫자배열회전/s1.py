import sys

sys.stdin = open('input.txt')


T = int(input())

i = 1
while i <= T:

    N = int(input())
    main_array = []

    # N x N 배열 생성
    j = 0
    while j < N:
        main_array.append(list(map(int, input().split())))
        j += 1

    # 90도 회전
    rotated_array1 = []
    for row1 in range(N):
        tmp_array1 = []
        for col1 in range(N):
            tmp_array1.append(main_array[N - 1 - col1][row1])
        rotated_array1.append(tmp_array1)

    # 180도 회전
    rotated_array2 = []
    for row2 in range(N):
        tmp_array2 = []
        for col2 in range(N):
            tmp_array2.append(main_array[N - 1 - row2][N - 1 - col2])
        rotated_array2.append(tmp_array2)

    # 270도 회전
    rotated_array3 = []
    for row3 in range(N):
        tmp_array3 = []
        for col3 in range(N):
            tmp_array3.append(main_array[col3][N - 1 - row3])
        rotated_array3.append(tmp_array3)

    # 출력하기
    print('#{}'.format(i))

    k = 0

    # N개의 줄
    while k < N:
        # 90 180 270 => 3개
        print(''.join(map(str, rotated_array1[k])), end=' ')
        print(''.join(map(str, rotated_array2[k])), end=' ')
        print(''.join(map(str, rotated_array3[k])), end=' ')

        print()

        k += 1
    i += 1