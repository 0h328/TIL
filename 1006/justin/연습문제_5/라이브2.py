def perm(n, m, k):
    """
    :param n: 순열의 길이
    :param m:
    :param k: 결정 할 위치
    :return:
    """

    if n == k:                  # 모든 자리가 결정이 됐다면
        print(*p)               # 출력
    else:
        for i in range(m):      # 주어진 숫자의 개수만큼 반복을 돌며
            if not u[i]:        # 아직 사용하지 않은 자리라면
                u[i] = 1        # 사용했다고 표시하고
                p[k] = arr[i]   # 그 숫자를 넣고
                perm(n, m, k+1) # 다음 자리를 결정하러 가자
                u[i] = 0        # 돌아와서 원상복구

p = [0] * 5
u = [0] * 5
arr = [1, 2, 3, 4, 5]
perm(5, 5, 0)
