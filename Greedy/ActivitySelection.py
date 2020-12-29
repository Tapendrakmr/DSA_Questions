# Input
def activitySelctionJob(Arr):

    count = 0
    i = 0
    for j in range(1, len(Arr)):

        if Arr[j][0] >= Arr[i][1]:
            print("Selcted value  ", Arr[j][0], Arr[j][1])
            count += 1
            i = j
    print("Number of job he can do", count)


jobs = []
for i in range(int(input("Enter number of jobs :"))):
    x = [int(x) for x in input("Enter start and end time :").split(' ')]
    jobs.append(x)
jobs.sort(key=lambda x: x[1])
activitySelctionJob(jobs)
print(jobs)
