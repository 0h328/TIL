tc = int(input())

for t in range(1, tc + 1):
    result = 0
    N, HN = input().split()
    print("#{} ".format(t), end = '')
    for nh in HN:
        nh_list = [0, 0, 0, 0]
        idx = 3
        if '0' <= nh <= '9':
            while idx + 1:
                nh_list[idx] = int(nh) % 2
                nh = int(nh) // 2
                idx -= 1
        else:
            nh = ord(nh) - 55
            while idx + 1:
                nh_list[idx] = int(nh) % 2
                nh = int(nh) // 2
                idx -= 1

        for i in nh_list:
            print(i, end='')
    print()