import re

sum = 0
l = list()

file = open("regex_sum_824642.txt")
r = file.read()
x = re.findall("[0-9]+", r)
for i in x:
    y = int(i)
    l.append(y)

for k in l:
    sum = sum + k

print(sum)
