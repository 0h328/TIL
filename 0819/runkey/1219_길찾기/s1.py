import sys
sys.stdin = open('input.txt')

for _ in range(10):                                 # 10개의 테스트 케이스
    tc, length = map(int, input().split())          # 테스트 케이스 번호와  길의 총 개수
    input_list = list(map(int, input().split()))    # 순서쌍
    result_dic1 = {}                                # 한 개의 정점에서 선택할 수 있는 길의 개수가 2개를 넘어가지 않기에
    result_dic2 = {}                                # 2개의 딕셔너리를 선언함

    visited = [0 for _ in range(100)]               # 해당 정점(분기점)을 방문했는지 확인하는 리스트
                                                                    # 정점에서 갈 수 있는 길을 dict에 담기 위한 반복문,
    for idx in range(0, length * 2, 2):                             # 순서쌍이므로 length * 2번 반복
        try:                                                        # 기본적으로 result_dict1에 값을 담음
            if result_dic1[input_list[idx]]:                        # result_dict1에 input_list의 idx번 째 값이 key에 존재하면
                result_dic2[input_list[idx]] = input_list[idx + 1]  # result_dict2에 해당 key, value 값을 저장함
        except KeyError:                                            # result_dict1에 해당 키 값이 없으면 KeyError가 나므로
            result_dic1[input_list[idx]] = input_list[idx + 1]      # result_dict1에 해당 key, value 값을 저장함

    result = 0                                      # result에 결과 값을 담음
    idx = 0                                         # idx에 현재 노드 값 저장
    stack = []                                      # stack에 지나간 노드 값을 저장
    for _ in range(400):                            # 정점(분기점)의 개수가 최대 100개, 한 엣지당 2번 방문 가능, 한 노드당 최대 2개이므로 최대 400개
        if visited.count(4):                        # 정상적으로 돌면 visited는 최대 3번 방문이므로, 4번 이상 반복하면 도착 못함으로 판단
            break                                   # for 문 빠져나감
        try:                                        # 일단 시도
            if visited[idx] == 0:                   # visited[idx]가 0이면
                visited[idx] = 1                    # visited[idx]를 1로 만들어줌
                if result_dic1[idx]:                # 만약 result_dict1[idx]에 값이 있다면
                    stack.append(idx)               # stack에 idx값을 추가
                    idx = result_dic1[idx]          # idx가 result_dict1의 idx key의 value값을 저장
            else:                                   # visited[idx]가 1이면
                visited[idx] += 1                   # visited[idx]를 1 추가함
                if result_dic2[idx]:                # result_dict2[idx]가 있으면
                    idx = result_dic2[idx]          # idx에 result_dict2[idx]를 넣어줌
                    stack.append(idx)               # stack에 idx를 추가

        except KeyError:                            # KeyError가 발생하면
            try:                                    # 일단 시도
                visited[idx] += 1                   # visited[idx]에 1을 더해줌
                if result_dic2[idx]:                # result_dict2[idx]가 있으면
                    idx = result_dic2[idx]          # idx에 result_dict2[idx]를 넣음
                    stack.append(idx)               # stack에 idx 추가
            except KeyError:                        # KeyError가 발생하면
                try:
                    idx = stack.pop()               # idx에 stack의 맨 윗값을 넣음
                    result = 0                      # result에 0을 넣음
                except IndexError:                  # 더 이상 pop할 게 없는데 pop을 하면
                    break                           # 길이 없는 것이므로 break
        finally:                                    # 무조건 실행
            if idx == 99:                           # idx가 99이면
                result = 1                          # result에 1을 넣음
                break                               # for 탈출
    print("#{} {}".format(tc, result))              # 결과 print