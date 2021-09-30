tc = int(input())

for t in range(1, tc + 1):
    result = 0
    N, M = map(int, input().split())
    print("#{} ".format(t), end = '')
    m_list = []
    while M:
        m_list.append(M % 2)
        M //= 2
    flag = 0
    try:
        for i in m_list[:N]:
            if i == 1:
                flag += 1
    except IndexError:
        flag = 0
    finally:
        if flag == N:
            print("ON")
        else:
            print("OFF")