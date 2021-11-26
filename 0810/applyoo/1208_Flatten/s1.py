import sys
sys.stdin = open('input.txt')

def flatten(arr, dump):
    counting = [0] * 101
    maxi = 0 # 최소값 미리 선언
    mini = 101 # 최대값 미리 선언
    dump_max = dump # dump 복사

    for i in arr: # counting하면서 최대값, 최소값 찾기
        if mini > i: mini = i
        elif maxi < i: maxi = i
        counting[i] += 1

    while dump: # 블럭이 가장 적은 칸에 있는 블럭을 쌓는 과정과 비슷
        count = counting[mini]
        if dump >= count: # 다 옮길 수 있는 경우(등호 매우 중요함)
            counting[mini+1] += count # 한 칸 높이기
            # counting[mini] = 0 => 굳이 필요 없음(옮긴 값 0으로 만드는 것)
            dump -= count # 옮긴만큼 dump에 -
            mini += 1 # 최소 층 +1
        else: # 다 옮길 수 없는 경우
            break # 최소층은 변동 없음

    while dump_max: # 블럭이 가장 많은 칸에 있는 블럭을 옮기는 과정과 비슷
        count = counting[maxi]
        if dump_max >= count: # 다 옮길 수 있는 경우(등호 매우 중요함)
            counting[maxi - 1] += count # 한 칸 낮추기
            # counting[maxi] = 0 => 굳이 필요 없음
            dump_max -= count # 옮긴만큼 dump에 -
            maxi -= 1 # 최고 층 -1
        else: # 다 옮길 수 없는 경우
            break # 최대층은 변동 없음

    # 만약, 같은 층을 만들고도 dump가 남았다면 멈춰야 하나 해당 로직은 안멈추기에
    # 이를 확인하는 if ~ else문 추가
    if maxi > mini:
        return maxi - mini
    else:
        return 0

for test in range(1, 11):
    dump = int(input())
    arr = list(map(int, input().split()))
    print('#{} {}'.format(test, flatten(arr, dump)))