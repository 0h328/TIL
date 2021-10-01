tc = int(input())

for t in range(1, tc + 1):
    result = 0
    M = float(input())
    print("#{} ".format(t), end = '')

    m_list = []
    while M:
        m_list.append(int(M * 2))
        M *= 2
        if int(M):
            M -= 1
        if len(m_list) > 12:
            break
    if len(m_list) > 12:
        print("overflow")
    else:
        for i in m_list:
            print(i, end="")
        print()