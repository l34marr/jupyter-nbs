x = range(1, 10)
y = range(1, 10)

for i in x:
    line = ''
    for j in y:
        line += '%s X %s = %s\t' % (i, j, i*j)
    print(line)
