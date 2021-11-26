import sys
sys.stdin = open('input.txt')

def cal(nums):
    global cnt
    global ans

    if ans[nums-1] == '*':
        temp_nums1 = int(ans.pop(nums-2))
        temp_nums2 = int(ans.pop(nums-1))
        temp_nums3 = temp_nums1 * temp_nums2
        nums = nums - 2
        cnt = nums
        ans[nums] = temp_nums3

    elif ans[nums-1] == '+':
        temp_nums1 = int(ans.pop(nums-2))
        temp_nums2 = int(ans.pop(nums-1))
        temp_nums3 = temp_nums1 + temp_nums2
        nums = nums - 2
        cnt = nums
        ans[nums] = temp_nums3

    elif ans[nums-1] == '/':
        temp_nums1 = int(ans.pop(nums - 2))
        temp_nums2 = int(ans.pop(nums-1))
        temp_nums3 = temp_nums1 / temp_nums2
        nums = nums - 2
        cnt = nums
        ans[nums] = temp_nums3

    else:
        temp_nums1 = int(ans.pop(nums-2))
        temp_nums2 = int(ans.pop(nums-1))
        temp_nums3 = temp_nums1 - temp_nums2
        nums = nums - 2
        cnt = nums
        ans[nums] = temp_nums3

def in_order(node):
    global ans
    global cnt

    if len(WORD[node]) == 4:
        in_order(int(WORD[node][2]))
        # 중위
        cnt += 1
        ans.append(WORD[node][1])
        in_order(int(WORD[node][3]))
        # > 계산
        cal(cnt)
    else:
        cnt += 1
        ans.append(WORD[node][1])

for i in range(10):
    T = int(input())
    ans = [0]
    WORD = [0] + [list(map(str, input().split())) for _ in range(T)]
    cnt = 0
    in_order(1)
    print('#{} {}'.format(i + 1, int(ans[1])))