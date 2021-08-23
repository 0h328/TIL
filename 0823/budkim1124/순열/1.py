def f(i, N, r):
    if i == r:  #N:      # 순열 완성
        print(P[0:r])   # r개만 출력
    else:           # i번 원소값 결정
        for j in range(i, N):       # 자신부터 오른쪽 원소와 교환
            P[i], P[j] = P[j], P[i]
            f(i+1, N,r)
            P[i], P[j] = P[j], P[i]


P = [1,2,3,4,5]
r = 3
f(0,len(P), r)