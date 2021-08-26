import sys  # 언호님이 봐주신 코드

sys.stdin = open('input.txt')

for _ in range(10):  # 10개의 테스트 케이스
    tc, length = map(int, input().split())  # 테스트 케이스 번호와  길의 총 개수
    input_list = list(map(int, input().split()))  # 순서쌍
    result_dic1 = {}  # 한 개의 정점에서 선택할 수 있는 길의 개수가 2개를 넘어가지 않기에
    result_dic2 = {}  # 2개의 딕셔너리를 선언함

    visited = [0 for _ in range(100)]  # 해당 정점(분기점)을 방문했는지 확인하는 리스트

    # 정점에서 갈 수 있는 길을 dict에 담기 위한 반복문,
    for idx in range(0, length * 2, 2):  # 순서쌍이므로 length * 2번 반복
        try:  # 기본적으로 result_dict1에 값을 담음
            if result_dic1[input_list[idx]]:  # result_dict1에 input_list의 idx번 째 값이 key에 존재하면
                result_dic2[input_list[idx]] = input_list[idx + 1]  # result_dict2에 해당 key, value 값을 저장함
        except KeyError:  # result_dict1에 해당 키 값이 없으면 KeyError가 나므로
            result_dic1[input_list[idx]] = input_list[idx + 1]  # result_dict1에 해당 key, value 값을 저장함

    # get 으로 수정하면 좋을거 같음

    result = 0  # 찾으면 1, 못찾으면 0
    idx = 0  # 인덱스 - 시작 노드
    stack = []  # 스택  - 방문한거를 스택에 쌓음

    # 0 -> 1 -> 2 -> 1 -> 3 -> 1  0 -> 1(1) -> 2
    -> 3
for _ in range(2 ** 100):  # 정점(분기점)의 개수가 최대 100개
    if visited.count(4):  # 
        break
    try:  #
        if visited[idx] == 0:  # 출발값이 방문하지 않았으면 6-- 아까 갔으므로 1이라 안감
            visited[idx] = 1  # 방문으로 변경
            if result_dic1[idx]:  # 1-- 1번 리스트에서 가는 길이 있으면 
                stack.append(idx)  # 스택에 추가
                idx = result_dic1[idx]  # 시작노드 변경


        elif visit:  # 출발값이 방문했으면 7-- 현재 위치 방문 +1 / 다음길을 찾음 / 없으면 딕셔너리 키를 못 찾아서 에러 발생 11-- 0번 노드에서 탐색, 두번째가 없음
            visited[idx] += 1  # ?? 방문을 추가
            if result_dic2[idx]:  # 2번째 값이 있으면
                idx = result_dic2[idx]  # 시작노드 변경
                stack.append(idx)  # 스택에 값 추가

    # 0 -> 1 -> 2 (?) -> 1

    except KeyError:  # 2-- 다음 갈 길이 없으면 에러 발생 (딕셔너리 키값이 없어서) 8-- 방문했던곳 하나 더 추가 12-- 두번째도 없으므로 에러
        try:  #
            visited[idx] += 1  # 방문했던곳 하나 더 추가 (필요가..?)
            if result_dic2[idx]:  # 3-- 첫번째에서도 갈길이 없는데, 두번째꺼를 찾으면 에러 또 발생 9-- 두번째꺼 없었는데 또 탐색으로 오류
                idx = result_dic2[idx]  # 
                stack.append(idx)  # 
        except KeyError:  # 4-- 에러 발생
            idx = stack.pop()  # 5-- 더이상 길 없는곳 노드에서 뒤로 감  (예시의 1번 노드를 꺼냄) 10-- 이전 방문한곳으로 이동 (예시 0번) 13-- 더이상 이전 노드가 없음 방문을 못했는데 결과가 0
            result = 0  # 
        finally:  # 
            if idx == 99:  # 
                result = 1  # 
                break  # 
    finally:  # 
        if idx == 99:  # 
            result = 1  # 
            break  # 

print("#{} {}".format(tc, result))  #