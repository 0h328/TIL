from collections import deque


T = int(input())

for tc in range(1, T + 1):
    p_d, p_1, p_3, p_y = map(int, input().split())
    data = list(map(int, input().split()))
    queue = deque()

    for i in range(12):
        if not data[i]:
            continue
        if not queue:
            queue.append((data[i] * p_d, [i]))
            queue.append((p_1, [i]))
            queue.append((p_3, [i, i + 1, i + 2]))
        else:
            while queue[0][1][0] != i:
                cur_price, chk = queue.popleft()
                if i in chk:
                    queue.append((cur_price, chk))
                    continue
                queue.append((cur_price + data[i] * p_d, [i]))
                queue.append((cur_price + p_1, [i]))
                queue.append((cur_price + p_3, [i, i + 1, i + 2]))

    ans = list(queue)
    ans.sort(key=lambda x: x[0])
    ans = ans[0][0]
    if ans > p_y:
        ans = p_y
    print("#{} {}".format(tc, ans))
