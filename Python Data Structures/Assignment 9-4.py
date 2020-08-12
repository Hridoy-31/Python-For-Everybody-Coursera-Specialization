name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count = dict()

for line in handle:
    if line.startswith('From '):
        line = line.split()
        x = line[1]
        count[x] = count.get(x,0) + 1

commit = None
val = None

for k,v in count.items():
    if val is None or v > val:
        commit = k
        val = v

print(commit, val)
