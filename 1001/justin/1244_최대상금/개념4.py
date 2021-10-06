#1-4. 같은 높이에서 반복이 나오면 다음은 계산하지 않음

def solve(k):                                       # K: 현재 교환 횟수
    global ans
    num = int(''.join(map(str, arr)))
    if num in visited[k]: return                    # 높이 k -> k번 교환해서 나온 값 -> 만약 num이 visited에 있으면 그 밑은 더 고려하지 않아도 됨
    visited[k].add(num)                             # 안나왔다고 하면 넣어 놓음(다음에 방문하지 않음)
    if k == cnt:                                    # 다 교환 했다면
        ans = max(ans, num)
        print(ans)
        # if ans < num:                               # 최댓값 갱신
        #     ans = num
        #     print(num)
    else:
        for i in range(N-1):                        # i ~ N-2
            for j in range(i+1, N):                 # i+1 ~ N-1
                arr[i], arr[j] = arr[j], arr[i]     # 바꾸고
                solve(k+1)                          # 다음 높이 확인
                arr[i], arr[j] = arr[j], arr[i]     # 원상복구

# 5C2
arr = [4, 5, 6, 7, 8, 9]
N = len(arr)
cnt = 2                                     # 교환 횟수 -> 2라면? -> 2번 교환 발생
ans = 0                                     # 교환 횟수 체크
visited = [set() for _ in range(11)]        # 중복 제거를 위해 set 활용 (인덱스 별 set이 의미하는 것은 교환 횟수 -> 0번 인덱스는 0회 교환 했을 때의 조합된 수 / 1번 인덱스는 1회 교환 했을 때의 조합된 수..)
solve(0)                                    # 0번 교환부터 시작 -> k번 교환이 발생한다면?
print(ans)