def binarySearch(job, start_index):
    lo = 0
    hi = start_index - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if job[mid][1] <= job[start_index][0]:
            if job[mid + 1][1] <= job[start_index][0]:
                lo = mid + 1
            else:
                return mid
        else:
            hi = mid - 1
    return -1


def schedule(job):
    job = sorted(job, key=lambda j: j[1])  # sort based on finish times
    table = [0 for _ in range(n)]
    table[0] = job[0][2]

    for i in range(1, n):
        inclProfit = job[i][2]
        l = binarySearch(job, i)
        if l != -1:
            inclProfit += table[l]
        table[i] = max(inclProfit, table[i - 1])

    return table[n - 1]


n = int(input("Enter the no of jobs to be scheduled:"))

# list of 3-tuple
job = []
for _ in range(n):
    start, finish, value = (input("Enter the start time, finish time  and value(start finish value):")).split()
    start = int(start)
    finish = int(finish)
    value = int(value)
    job.append((start, finish, value))
