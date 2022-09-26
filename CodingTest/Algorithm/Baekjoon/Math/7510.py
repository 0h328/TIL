# get number of trials
n = int(input())
# get three number inputs per trial
for i in range(n):
    triangle = sorted(list(map(int, input().split())))

    if triangle[0]**2 + triangle[1]**2 == triangle[2]**2:
        print("Scenario #{}:".format(i+1))
        print("yes")
    else:
        print("Scenario #{}:".format(i+1))
        print("no")
    print()
