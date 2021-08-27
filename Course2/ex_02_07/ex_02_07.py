name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

dis = dict()
for line in handle:
    if not line.startswith('From '):
        continue
    lst = line.split()
    time = lst[5]
    stime = time.split(':')
    hr = stime[0]
    dis[hr] = dis.get(hr,0) + 1

dis.items()

for key,value in sorted(dis.items()):
    print(key,value)
