name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count = dict()
ls = list()
for line in handle:
    if line.startswith("From "):
        line = line.split()
        l = line[5]
        l = l.split(":")
        lp = l[0]
        count[lp] = count.get(lp,0) + 1
        
x = sorted(count.items())

for k,v in x:
    print(k, v)
