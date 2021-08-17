import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, 2):

    N = int(input())
    arr = list(map(int, input().split()))

    # 버블 정렬
    # 소요시간: 37분 34초
    # 하나씩 바꾸어나가면서 한 턴 끝나면 맨 뒤에 인덱스 무시하고 다시 시작
    # 첫 위치에 도달하면 끝
    for i in range(len(arr)-1):
        j = 0
        while N-1 > j:
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            j += 1
        N -= 1

    print('#{} {}'.format(tc, ' '.join(map(str, arr))))

    # 카운팅 정렬 도무지 이해가..
    # count number of each occurrences in the array
    # add each number to the right accumulatively
    # 각 숫자의 개수를 세었기 때문에, 최종으로 정렬 될 수의 마지막 인덱스보다 숫자1만큼 더 높다. 고로 각 인덱스 원소값 -1
    # 영후님께 물어보겠습니다!
    # print(arr)
    # minV, maxV = min(arr), max(arr)
    # cnt = []
    # for i in range(minV, maxV+1):
    #     num = arr.count(i)
    #     cnt.append(num)
    # print(cnt)
    #
    # for i in range(len(cnt)-1):
    #     cnt[i+1] += cnt[i]
    #     cnt[i] -= 1                 # 각 숫자의 개수를 세었기 때문에 최종으로 정렬 될 수의
    # cnt[-1] -= 1                    # 마지막 인덱스보다 숫자1만큼 더 높다. 고로 각 인덱스 원소값 -1
    # print(cnt)
    #
    # ans = [0] * N
    # for i in arr[::-1]:
    #     temp = cnt[i]
    #     ans[N-1] = temp
    #     N -= 1
    # print(ans)
    #
    # ans = [0] * N
    # for i in range(len(arr)-1, -1, -1):
    #     ans[i] = cnt[]





