fname = input("Enter file name: ")
fh = open(fname)

for line in fh:
	nline = line.rstrip()
	print(nline.upper())
