import sys
sys.stdin = open('input.txt')

for num in range(1,11):
    N = int(input())
    h_lists = list(map(int, input().split()))

    if sum(h_lists) % len(h_lists) != 0:

        for i in range(N):
            h_lists[h_lists.index(max(h_lists))] = max(h_lists) - 1
            h_lists[h_lists.index(min(h_lists))] = min(h_lists) + 1

        print("#{} {}".format(num, max(h_lists) - min(h_lists)))

    else:

        for i in range(N):

            # for h_list in h_lists:
            #     if h_list == sum(h_lists)/len(h_lists):
            #         print("#{} {}".format(num, 0))

            h_lists[h_lists.index(max(h_lists))] = max(h_lists) - 1
            h_lists[h_lists.index(min(h_lists))] = min(h_lists) + 1

        print("#{} {}".format(num, max(h_lists) - min(h_lists)))



