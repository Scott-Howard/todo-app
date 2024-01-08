filenames = ['a.txt','b.txt','c.txt']

for files in filenames:
    file = open(files,'r')
    qw = file.read()
    print(qw)

