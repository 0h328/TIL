import sys
sys.stdin = open('input.txt')

def is_babygin(arr, count):
    if count == 2:
        return 1
    else:
        for i in range(len(arr)):
            if arr[i] > 0:
                # is_triplet
                if arr[i] >= 3:
                    temp = arr.copy()
                    temp[i] -= 3
                    return is_babygin(temp, count+1)
                # is_run
                if i < 8 and arr[i+1] > 0 and arr[i+2] > 0:
                    temp = arr.copy()
                    temp[i]-=1
                    temp[i+1]-=1
                    temp[i+2]-=1
                    return is_babygin(temp, count+1)

    return 0

for _ in range(int(input())):
    counts = [0]*10
    for s in input():
        counts[int(s)] += 1
    
    print(is_babygin(counts, 0))