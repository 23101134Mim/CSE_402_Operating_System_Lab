process = ["P1", "P2", "P3", "P4", "P5"]
at = [3, 0, 2, 1, 4]
bt = [4, 4, 3, 6, 2]
priority = [2, 0, 1, 1, 3]

n = len(process)

ct = [0]*n
wt = [0]*n
tat = [0]*n
tq = 3
remaining = bt.copy()
time = 0
completed = 0

while completed < n:
    x = -1
    for i in range(n):
        if at[i] <= time and remaining[i] > 0:
            if x == -1 or priority[i] < priority[x] or (priority[i] == priority[x] and at[i] < at[x]):
                x = i
    if x == -1:
        time += 1
    else:
        if remaining[x] > tq:
            time += tq
            remaining[x] -= tq
        else:
            time += remaining[x]
            remaining[x] = 0
            ct[x] = time
            completed += 1

for i in range(n):
    tat[i] = ct[i] - at[i]
    wt[i] = tat[i] - bt[i]

print("Process\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    print(f"{process[i]}\t{at[i]}\t{bt[i]}\t{ct[i]}\t{tat[i]}\t{wt[i]}")


print("\nAverage TAT =", sum(tat)/n)
print("Average WT =", sum(wt)/n)
