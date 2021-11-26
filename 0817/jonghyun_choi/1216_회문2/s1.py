import sys
sys.stdin = open('input.txt')

def find_word(data_list, length):
    ind = 0
    while ind < 100 - length + 1:
        for data in data_list:
            if data[ind:ind+length] != data[ind:ind+length][::-1]:
                continue
            else:
                return length
        ind += 1
    return 0


for _ in range(10):
    N = int(input())
    alpha_list = [list(input()) for _ in range(100)]
    zip_list = list(zip(*alpha_list))
    max_len = 100
    while max_len > 0:
        if find_word(alpha_list, max_len) or find_word(zip_list,max_len):
            break
        max_len -= 1
    print('#{} {}'.format(N, max_len))
