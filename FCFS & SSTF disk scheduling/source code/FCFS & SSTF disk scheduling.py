req  = [0, 30, 41, 62, 14, 20]
head = 20


req = [r for r in req if r != head]

# FCFS
total_fcfs = 0
cur = head
for r in req:
    total_fcfs += abs(r - cur)
    cur = r

# SSTF
remaining = req.copy()
total_sstf = 0
cur = head
while remaining:
    closest = min(remaining, key=lambda x: abs(x - cur))
    total_sstf += abs(closest - cur)
    cur = closest
    remaining.remove(closest)

print("FCFS Total Seek =", total_fcfs)
print("SSTF Total Seek =", total_sstf)

if total_sstf < total_fcfs:
    print("SSTF is better (less seek time)")
else:
    print("FCFS is better (less seek time)")
