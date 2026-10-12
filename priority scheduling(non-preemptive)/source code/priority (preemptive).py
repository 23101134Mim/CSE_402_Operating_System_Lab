process = ["p1", "p2", "p3", "p4"]
at = [0,3,1,2]
bt = [3,2,2,1]
priority = [4,0,2,1]

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

            if x == -1 or priority[i] < priority[x]:
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

non_P_avg_tat = sum(tat)/n
non_p_avg_wt = sum(wt)/n

print("\nAverage TAT =", non_P_avg_tat)
print("Average WT =", non_p_avg_wt)
print("\n")
