total = 0
count = 0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    nline = line.rstrip()
    num = nline[20:]
    fnum = float(num)
    total = total + fnum
avg = total/count
print("Average spam confidence:",avg)
#print(count)
#print(num)
#print(nline)
