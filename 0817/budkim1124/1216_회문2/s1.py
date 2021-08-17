import sys
sys.stdin = open('input.txt')

for num in range(10):
    number = int(input())
    words = [list(map(str, input())) for _ in range(100)]
    col_words = list(zip(*words))

    max_len = 0
    for i in range(100):
        for n in range(3, 101):
            for k in range(100):
                tmp1 = []
                tmp2 = []
                if k + n <= 100:
                    tmp1 = words[i][k:k+n]
                    if list(tmp1) == list(reversed(tmp1)) and max_len < len(tmp1):
                        max_len = len(tmp1)

                if k + n <= 100:
                    tmp1 = col_words[i][k:k+n]
                    if list(tmp1) == list(reversed(tmp1)) and max_len < len(tmp1):
                        max_len = len(tmp1)

    print("#{} {}".format(num+1, max_len))

