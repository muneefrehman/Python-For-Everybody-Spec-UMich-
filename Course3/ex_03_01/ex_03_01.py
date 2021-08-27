import re


file = input("Enter File: ")
if len(file) < 1: file = "regex_sum_982338.txt"

sum = 0
handle = open(file)
for line in handle:
    y = re.findall('[0-9]+',line)
    for num in y:
        sum = sum + int(num)

print(sum)
