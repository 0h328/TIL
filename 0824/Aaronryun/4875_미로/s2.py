for test in range(1, 1 + int(input())):
    x, y = list(map(int, input().split()))

    max_data = 0
    h_max = min(x, y) / 2
    h = h_max
    while h >0:
        cal = (x - (2 * h)) * (y - (2 * h)) * h
        if max_data < cal:
            max_data = cal
        h -= 0.0001
    print('#{} {:.6f}'.format(test, max_data))

# 이게 아니라고....?