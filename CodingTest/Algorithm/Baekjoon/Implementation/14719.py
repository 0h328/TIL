import sys
sys.stdin = open('input.txt')

H, W = map(int, input().split())
arr = list(map(int, input().split()))
res = 0
for i in range(1, W-1): # 블록 사이만 체크하므로, 양 끝은 체크할 필요 없음
    l_h = max(arr[:i])  # 현재 기준으로 왼쪽 블록의 가장 높은 블록
    r_h = max(arr[i+1:])# 현재 기준으로 오른쪽 블록의 가장 높은 블록
    if arr[i] < min(l_h, r_h):  # 현재 기준으로 양 옆의 높은 블록 중 낮은 블록으로 체크
        res += min(l_h, r_h) - arr[i]   # 해당 블록이랑 기준 블록을 차감하여 누적

print(res)