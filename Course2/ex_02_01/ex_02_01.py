text = "X-DSPAM-Confidence:    0.8475";
pos = text.find(':')
#print(pos)
ext = text[pos+1:]
#print(ext)
ans = float(ext)
print(ans)