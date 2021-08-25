import sys

sys.stdin = open('input.txt')

def permutation(idx):
    global min_data, msum  # 최소값을 저장할 공간과 전체 합을 저장할 공간을 글로벌로 불러오기

    if min_data < msum:  # 최소값으로 지정한 값보다 합이 더 커지는 경우  중지 런타임에러방지
        return

    if idx == N:  # 합보다 최소값이 큰경우 치환해주고 리턴
        if min_data > msum:
            min_data = msum
        print(check)
        return

    for i in range(N): # 순열구하기
        if check[i] == 0:
            check[i] = 1
            msum += data[idx][i] # 체크한 영역의 가로의 인덱스를 가지는 곳을 더한다.
            permutation(idx + 1) # 하나 더 올리면 세로를 내려간다
            check[i] = 0 # 돌아가기 위해서 기존의 값을 0으로 바꾸고
            msum -= data[idx][i] # 더한 값만큼도 빼준다


for test in range(1, 1 + int(input())):
    N = int(input())

    data = [list(map(int, input().split())) for _ in range(N)]

    check = [0] * N
    msum = 0
    min_data = 9 * N # 10보다 작은 자연수가 들어온다 모두 9가 들어오는 경우가 가장 큰값

    permutation(0)
    print('#{} {}'.format(test, min_data))
