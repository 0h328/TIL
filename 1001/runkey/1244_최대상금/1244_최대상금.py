tc = int(input())

for t in range(1, tc + 1):
    result = 0
    num, change = map(int, input().split())

    # num_list에 num의 각 자리를 담기
    num_list = [0] * len(str(num))
    for i in range(len(str(num)) - 1, -1, -1):
        num_list[i] = num % 10
        num //= 10


    for c in range(1, change + 1):
        idx = 0
        # min(num_list), max(num_list) 풀어 쓰기
        min_num, max_num = num_list[0], num_list[idx]
        min_idx, max_idx = 0, idx
        print(f'c = {c}, min_num = {min_num}, max_num = {max_num}, min_idx = {min_idx}, max_idx = {max_idx}')
        for i in range(1, len(num_list) - idx):
            if min_num > num_list[i]:
                min_num = num_list[i]
                min_idx = i
            if max_num <= num_list[i]:
                max_num = num_list[i]
                max_idx = i

        print(f'c = {c}, min_num = {min_num}, max_num = {max_num}, min_idx = {min_idx}, max_idx = {max_idx}')
        print(num_list)
        if min_idx < max_idx:
            num_list[min_idx], num_list[max_idx] = num_list[max_idx], num_list[min_idx]
        idx += 1
    temp = ''
    for i in range(len(num_list)):
        temp += str(num_list[i])
    result = int(temp)
    print("#{} {}".format(t, result))