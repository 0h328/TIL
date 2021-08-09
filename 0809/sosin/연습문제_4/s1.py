import sys
sys.stdin = open('input.txt')

def is_babygin(arr, count):
    print(arr)
    if count == 2:
        return True
    else:
        for i in range(len(arr)):
            if arr[i] > 0:
                # is_triplet
                if arr[i] >= 3:
                    arr[i] -= 3
                    return is_babygin(arr, count+1)
                # is_run
                elif i < 8 and arr[i+1] > 0 and arr[i+2] > 0:
                    arr[i]-=1
                    arr[i+1]-=1
                    arr[i+2]-=1
                    return is_babygin(arr, count+1)

    return False

for _ in range(int(input())):
    counts = [0]*10
    for s in input():
        counts[int(s)] += 1
    
    print(is_babygin(counts, 0))