import sys
sys.stdin = open('input.txt')

def find_word(data_list,length):
    ind = 0
    cnt = 0
    while ind < 8 - length + 1:
        for data in data_list:
            if data[ind:ind + length] != data[ind:ind + length][::-1]:
                continue
            else:
                cnt += 1
        ind += 1
    return cnt


for case in range(10):
    N = int(input())
    data_list = [list(input()) for _ in range(8)]
    zip_list = list(zip(*data_list))

    res = 0
    res += find_word(data_list, N)
    res += find_word(zip_list, N)

    print('#{} {}'.format(case + 1, res))

