processes = [["P1",3,5],
            ["P2",2,4],
            ["P3",4,3],
            ["P4",1,2],
            ["P5",5,3]]

processes.sort(key=lambda x:x[1])
time = 0
total_tat = 0
total_wt =0
print("PID\tAT\tBT\tCT\tTAT\tWT")
for pid,at,bt in processes:
    if time < at:
      time =at
    time= time + bt
    ct= time
    tat = ct-at
    wt = tat - bt
    total_tat += tat
    total_wt += wt
    print(pid, "\t", at,"\t",bt,"\t",ct,"\t",tat,"\t",wt)
    avg_tat =total_tat/len(processes)
    avg_wt = total_wt / len(processes)
    print("\nAverage TAT =",avg_tat)
    print("\nAverage WT =", avg_wt)
