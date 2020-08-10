# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
x = fh.read()
x = x.rstrip()
print(x.upper())
