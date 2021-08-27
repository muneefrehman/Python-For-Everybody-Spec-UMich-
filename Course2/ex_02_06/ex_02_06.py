file = input("Enter file:")
if len(file) < 1 : file = "mbox-short.txt"
handle = open(file)

counts = dict()
for line in handle:
    if not line.startswith("From "):
        continue
    lst = line.split()
    name = lst[1]
    counts[name] = counts.get(name,0) + 1


bigword = None
bigcount = None
for email,count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = email
print(bigword,bigcount)
