import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())  # 화덕의 크기, 피자 개수
    Ci = []
    for num, pizza in enumerate(list(map(int, input().split())), 1):  # 피자 치즈 양
        Ci.append([num, pizza])
    Q = Ci[:N]  # 화덕
    Ci = Ci[N:]  # 남아있는 피자

    while len(Q) > 1:  # 화덕에 피자가 2개 이상일 때
        Q[0][1] //= 2  # 치즈 양이 2로 나눠짐
        if Q[0][1] == 0:  # 치즈가 0이 됐을 때
            Q.pop(0)
            if Ci:  # 남아있는 피자가 있다면
                Q.append(Ci.pop(0))  # 남아있는 피자 첫번째를 화덕에 넣어줌
        else:
            Q.append(Q.pop(0))  # 치즈가 0이 아닐 때 맨마지막에 도로 넣기

    print('#{} {}'.format(t, Q[0][0]))
