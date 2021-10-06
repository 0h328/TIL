import sys
sys.stdin = open('input.txt')

T = int(input())

for case in range(T):
    data = list(map(int, input().split()))
    cur_A = [0] * 12
    cur_B = [0] * 12
    run_a = run_b = tri_a = tri_b = 0
    for i in range(len(data) // 2):
        a, b = data[i * 2], data[i * 2 + 1]
        cur_A[a] += 1
        cur_B[b] += 1
        if a <= 1:
            cur_A[a + 10] += 1
        if b <= 1:
            cur_B[b + 10] += 1

        if i >= 2:
            idx = 0
            while idx < 10:
                if cur_A[idx] >= 3:
                    cur_A[idx] -= 3
                    tri_a += 1
                    continue

                if cur_B[idx] >= 3:
                    cur_B[idx] -= 3
                    tri_b += 1
                    continue

                if cur_A[idx] >= 1 and cur_A[idx + 1] >= 1 and cur_A[idx + 2] >= 1:
                    cur_A[idx] -= 1
                    cur_A[idx + 1] -= 1
                    cur_A[idx + 2] -= 1
                    run_a += 1
                    continue

                if cur_B[idx] >= 1 and cur_B[idx + 1] >= 1 and cur_B[idx + 2] >= 1:
                    cur_B[idx] -= 1
                    cur_B[idx + 1] -= 1
                    cur_B[idx + 2] -= 1
                    run_b += 1
                    continue

                idx += 1
        if run_a or run_b or tri_a or tri_b:
            break

    if not (run_a or run_b or tri_a or tri_b):
        print('#{} {}'.format(case + 1, 0))

    elif run_a + tri_a >= run_b + tri_b:
        print('#{} {}'.format(case + 1, 1))
    elif run_a + tri_a < run_b + tri_b:
        print('#{} {}'.format(case + 1, 2))


