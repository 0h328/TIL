import sys
sys.stdin = open('input.txt')

for _ in range(10):
    tc, length = map(int, input().split())
    input_list = list(map(int, input().split()))
    result_dic1 = {}
    result_dic2 = {}

    visited = [0 for _ in range(100)]

    for idx in range(0, length*2, 2):
        try:
            if result_dic1[input_list[idx]]:
                result_dic2[input_list[idx]] = input_list[idx + 1]
        except KeyError:
            result_dic1[input_list[idx]] = input_list[idx + 1]

    result = 0
    idx = 0
    stack = []
    for _ in range(100):
        try:
            if visited[idx] == 0:
                visited[idx] = 1
                if result_dic1[idx]:
                    stack.append(idx)
                    idx = result_dic1[idx]
            else:
                if result_dic2[idx]:
                    idx = result_dic2[idx]
                    stack.append(idx)

        except KeyError:
            try:
                if result_dic2[idx]:
                    idx = result_dic2[idx]
                    stack.append(idx)
            except KeyError:
                idx = stack.pop()
                result = 0
            finally:
                if idx == 99:
                    result = 1
                    break
        finally:
            if idx == 99:
                result = 1
                break
    print("#{} {}".format(tc, result))