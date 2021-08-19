import sys
sys.stdin = open('input.txt')

N = int(input())

for tc in range(N):
    M = input()
    num_arr = []
    num = 1
    total = 0
    for idx in range(len(M)):
        if M[idx]=='(':
            num_arr.append(1)
        else:
            num_arr.append(2)
    print(num_arr)
    new_arr = num_arr[::]
    for idx in range(len(M)-1):
        if num_arr[idx] == 1 and num_arr[idx+1] == 2:
            new_arr[idx] = 0
            new_arr[idx+1] = 0
    print(new_arr)
    new_num = 3
    for idx in range(len(M)):
        if new_arr[idx] == 2:
            for j in range(idx-1, -1, -1):
                if new_arr[j] == 1:
                    new_arr[idx] = new_num
                    new_arr[j] = new_num
                    new_num += 1
                    break
    max_num = max(new_arr)
    print(new_arr)

##여기까지가 리스트 만들기는 완료!!
    # print(new_arr.index(3))
    # print(new_arr.index(3))

    # new_arr[idx + 1:first_idx].count(0)
    # print(new_arr[2:9].count(0))
    for idx in range(len(M)-1, -1, -1):
        first_idx = new_arr.index(max_num)
        if new_arr[idx] == max_num and first_idx < idx:
            count_laser = new_arr[first_idx:idx].count(0)
            count_laser //= 2
            total += (count_laser+1)
            count_laser = 0
            max_num -= 1
            if max_num < 3:
                break




    print(max_num)
    print(new_arr)
    print(total)