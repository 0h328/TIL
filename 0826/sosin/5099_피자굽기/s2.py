import sys
sys.stdin = open('input.txt')

for T in range(int(input())):
    N, M = map(int, input().split())
    # 화덕의 크기 N
    pizza = list(map(int, input().split()))

    circle_count = []
    for p in pizza:
        for i in range(1, 6):
            if p < 2**i:
                circle_count.append(i)
                break

    idx_list = [i for i in range(M)]

    while len(idx_list) > N:
        min_count = 9
        for i in range(N):
            min_count = min(min_count, circle_count[idx_list[i]])
        
        pop_idxs = []
        for i in range(N):
            circle_count[idx_list[i]]-=min_count
            if circle_count[idx_list[i]] == 0:
                pop_idxs.append(idx_list[i])

        for pi in pop_idxs:
            idx_list.pop(idx_list.index(pi))
        
    max_count = 0
    answer = -1
    for idx in idx_list:
        if max_count <= circle_count[idx]:
            max_count = circle_count[idx]
            answer = idx

    print('#{} {}'.format((T+1), answer+1))
