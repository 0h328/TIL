tc = int(input())

for t in range(1, tc + 1):
    result = 0
    num, change = map(int, input().split())

    # num_list에 num의 각 자리를 담기
    num_list = [0] * len(str(num))
    for i in range(len(str(num)) - 1, -1, -1):
        num_list[i] = num % 10
        num //= 10

    sidx = 0                    # 시작 인덱스
    eidx = len(num_list) - 1    # 끝 인덱스
    c = 1                       # 현재 교환 횟수
    while sidx < eidx:          # 시작 인덱스가 끝 인덱스보다 작을 때 까지 반복
        flag = 1    # 최소 인덱스 찾을 때 찾으면 더 안 찾게 하려구 만듦
        min_num, max_num = min(num_list[sidx:eidx + 1]), max(num_list[sidx:eidx + 1])   # 리스트에서 가장 작은 수와 큰 수를 저장
        min_idx, max_idx = sidx, eidx   # 가장 작은 값이 들어있는 인덱스, 가장 큰 값이 들어있는 인덱스
        cnt = 0                         # 최대 숫자 갯수
        for i in range(sidx, eidx + 1): # sidx부터 eidx까지 반복
            if flag and min_num == num_list[i]:     # 최소 인덱스 찾기, flag = 가장 작은 값을 찾는 즉시 더 이상 안 찾음
                min_idx = i             # 가장 작은 값의 인덱스 저장
                flag = 0                # 더 이상 if 문에 못 들어오게 0 저장
            if max_num == num_list[i]:  # 최대 인덱스 찾기
                max_idx = i             # 최대 인덱스는 가장 마지막 위치까지 가야함, 그래야 최종 수가 큰 수임
                cnt += 1                # 최대 숫자 갯수 + 1

        if sidx != max_idx and change - c == 0:     # 시작 인덱스 값이 최대가 아니고 마지막 교환일 때
            num_list[sidx], num_list[max_idx] = num_list[max_idx], num_list[sidx]   # 시작 인덱스 값과 최대값 위치 바꿈
            c += 1  # 마지막에 교환횟수가 남았다면 뒷자리 바꾸는 코드에 들어가지 않게 하기 위함
            break   # 처음부터 change가 1이거나 교환횟수가 마지막이면 while 빠져나감

        if sidx == max_idx: # 시작 인덱스랑 최대값 인덱스랑 같으면 교환할 게 없으므로
            sidx += 1       # 시작 인덱스를 + 1
            continue        # 다음 순회

        if cnt == 1 or min_idx > max_idx:   # 최대값 인덱스가 최소보다 앞에 위치하면
            num_list[sidx], num_list[max_idx] = num_list[max_idx], num_list[sidx]   # 최대값을 맨앞으로 옮김
            sidx += 1   # 맨 앞은 고정해야 하므로 sidx + 1
        elif min_idx <= max_idx:    # 최솟값 인덱스가 앞에 위치하면
            num_list[eidx], num_list[min_idx] = num_list[min_idx], num_list[eidx]   # 최솟값을 맨 뒤로 보내기
            eidx -= 1   # 맨 뒤는 이제 고정이므로 eidx - 1
        c += 1  # 교환횟수 1회 소진
    
    # end while
    overlap = 0 # 모든 인덱스를 다 돌고도 교환이 남을 시, 중복 숫자 있는지 판단 여부 => 중복 숫자가 있으면 그 숫자 유지 하면 된다.
    for i in range(len(num_list) - 1):
        for j in range(i + 1, len(num_list)):
            if num_list[i] == num_list[j]:
                overlap = 1 # 같은 숫자를 발견하면 overlap 1 표시 후 빠져 나감
                break

    if overlap != 1:    # 중복 숫자가 없을 때, 교환 횟수 다 소진할 때 까지 맨 뒤의 두자리만 계속 바꾸기
        while c < change + 1:
            num_list[len(num_list) - 2], num_list[len(num_list) - 1] = num_list[len(num_list) - 1], num_list[len(num_list) - 2]
            c += 1

    temp = ''   # 리스트를 출력하기 위해 문자를 담을 임시 변수
    for i in range(len(num_list)):
        temp += str(num_list[i])    # 앞에부터 하나씩 출력해서 temp에 문자로 더해줌
    result = int(temp)              # int로 변환 후 결과에 담음
    print("#{} {}".format(t, result))