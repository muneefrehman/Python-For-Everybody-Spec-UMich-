fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    pieces = line.split()
    for words in pieces:
        if words not in lst:
            lst.append(words)
lst.sort()
print(lst)
