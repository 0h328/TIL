import sys

sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())
    data = [list(map(str, input())) for _ in range(100)]

    max_length = 0
    for k in range(100):
        for i in range(100):
            for j in range(99, i-1, -1):
                if data[k][i] != data[k][j]:
                    continue
                else:
                    if data[k][i:j+1] == data[k][i:j+1][::-1]:
                        max_length = max(max_length, len(data[i:j+1]))
                        break
                    else:
                        continue

    tp_data = list(zip(*data))
    for k in range(100):
        for i in range(100):
            for j in range(99, i-1, -1):
                if tp_data[k][i] != tp_data[k][j]:
                    continue
                else:
                    if tp_data[k][i:j+1] == tp_data[k][i:j+1][::-1]:
                        max_length = max(max_length, len(data[i:j+1]))
                        break
                    else:
                        continue

    print('#{} {}'.format(tc, max_length))