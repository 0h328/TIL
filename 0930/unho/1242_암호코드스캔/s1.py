import sys
from collections import deque
sys.stdin = open('input.txt')


CODE_DICT = {
    (3, 2, 1, 1): 0,
    (2, 2, 2, 1): 1,
    (2, 1, 2, 2): 2,
    (1, 4, 1, 1): 3,
    (1, 1, 3, 2): 4,
    (1, 2, 3, 1): 5,
    (1, 1, 1, 4): 6,
    (1, 3, 1, 2): 7,
    (1, 2, 1, 3): 8,
    (3, 1, 1, 2): 9,
}


def search_code(bin_code):      # 코드 찾아냄
    num_li.clear()

    for width in range(1, 10):
        for i in range(8):
            end = len(bin_code) - (width * i * 7)
            start = end - (width * 7)

            if start < 0:
                start = 0
            if end < 0:
                end = 0
            
            tmp = bin_code[start:end]
            if not start:
                need = 7*width - len(tmp)
                tmp = '0' * need + tmp

            cnt = [0] * 4
            idx, value = 0, '0'
            for e in tmp:
                if e != value:
                    idx += 1
                    value = e
                cnt[idx] += 1
            
            if not cnt[3]:
                cnt[3] = 1
            
            for idx in range(4):
                cnt[idx] //= width
            
            result = CODE_DICT.get(tuple(cnt), -1)
            if result != -1:
                num_li.appendleft(result)
                # print(f'LOG --- NUM_LI : {num_li}')
            else:
                break
        if len(num_li) == 8:
            return bin_code[:start]
        else:       # 값 모두 찾아내면 종료
            return


def calc():
    tmp_answer = 0
    for i in range(8):
        if i == 7:
            tmp_answer += num_li[i]
        elif not i % 2:
            tmp_answer += (num_li[i] * 3)
        else:
            tmp_answer += num_li[i]
    
    if not tmp_answer % 10:
        return sum(num_li)
    else:
        return 0



T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    num_li = deque()
    use = set()
    answer = 0

    for _ in range(N):
        in_str = input().strip('0')

        if in_str:
            bin_code = bin(int(in_str, 16))[2:].rstrip('0')
            while bin_code:
                bin_code = bin_code.rstrip('0')
                if bin_code not in use:
                    use.add(bin_code)
                    bin_code = search_code(bin_code)
                    answer += calc()
    print(answer)
