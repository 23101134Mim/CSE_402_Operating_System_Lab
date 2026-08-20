process = ["p1", "p2", "p3", "p4", "p5"]
at = [2, 3, 0, 1, 1]
bt = [5, 1, 2, 3, 6]

n = len(process)
ct = [0] * n
wt = [0] * n
done = [0] * n
tat = [0] * n
time = 0
completed = 0

while completed < n:
    x = -1
    for i in range(n):
        if at[i] <= time and done[i] == 0:
            if x == -1 or bt[i] < bt[x]:
                x = i
    if x == -1:
        time += 1
    else:
        time = time + bt[x]
        ct[x] = time
        done[x] = 1
        completed += 1

for i in range(n):
    tat[i] = ct[i] - at[i]
    wt[i] = tat[i] - bt[i]

print("Process\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    print(process[i], "\t", at[i], "\t", bt[i], "\t", ct[i], "\t", tat[i], "\t", wt[i])

print("\nAverage TAT =", sum(tat)/n)
print("Average WT =", sum(wt)/n)
